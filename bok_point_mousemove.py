
import numpy as np
import pandas as pd
import compute_path as cp
from sklearn import mixture
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from bokeh.plotting import figure, curdoc
from bokeh.io import  push_notebook,output_notebook, show
from bokeh.models import ColumnDataSource, LabelSet,Ellipse, Column
from bokeh.models import PreText, CustomJS,HTMLTemplateFormatter, Circle
from bokeh.models import TapTool, Div, DataTable, TableColumn, TextInput
from bokeh.tile_providers import get_provider
from bokeh.models.tools import HoverTool
from bokeh.layouts import row, layout, column, widgetbox
from bokeh.events import Tap, MouseMove

from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler

import pyproj
from matplotlib import cm
import matplotlib
import matplotlib.pyplot as plt


def get_stations_old(X, Y):   
    d_lat, d_long = cp.MetersToLatLon(X, Y)
    
    # Prediction
    y_pred = gmm.predict_proba([[X, Y]])

    y_pred = np.where(y_pred>0.001)
    count_prob = []
    
    for i in np.unique(y_pred[0]):
        ind = y_pred[0]
        count_prob.append(y_pred[1][ind==i])
   
    # Affichage prédiction
    c = count_prob[0]
    c = list(c)
    paths_x, paths_y, dists = [], [], []
    for count, stations in enumerate(c):
        lab = station_names[stations]

        o_long, o_lat = station_coord[stations, :2]
        print(lab, o_long, o_lat)
        path, dist = cp.compute_path_euc(nodes, sg,
                               o_long,
                               o_lat,
                               d_long, 
                               d_lat)
        dists.append(np.round(dist*0.75, 2))
        linepath, intersections = cp.get_linepath(sg, path)
        x,y = cp.wgs84_to_web_mercator(linepath[:, 1], linepath[:, 0])
        listx, listy = x.tolist(), y.tolist()
        listx.reverse()
        paths_x.extend(listx)
        listx.reverse()
        paths_x.extend(listx)
        
        listy.reverse()
        paths_y.extend(listy)
        listy.reverse()
        paths_y.extend(listy)
    return c, paths_x, paths_y, dists
def get_stations_new(X, Y):   
    d_lat, d_long = cp.MetersToLatLon(X, Y)
    
    # Prediction
    y_pred = gmm.predict_proba([[X, Y]])

    y_pred = np.where(y_pred>0.001)
    count_prob = []
    
    for i in np.unique(y_pred[0]):
        ind = y_pred[0]
        count_prob.append(y_pred[1][ind==i])
   
    # Affichage prédiction
    c = count_prob[0]
    c = list(c)
    paths_x, paths_y, dists = [], [], []
    for count, stations in enumerate(c):
        dist = np.sqrt( (X-station_coord[stations,2])**2 + (Y-station_coord[stations,3])**2)
        dists.append(np.round(dist*0.75, 2))
        listx, listy = [X, station_coord[stations,2]], [Y, station_coord[stations,3]]
        paths_x.extend(listx)
        listx.reverse()
        paths_x.extend(listx)
        
        paths_y.extend(listy)
        listy.reverse()
        paths_y.extend(listy)
    return c, paths_x, paths_y, dists
import pickle as pickle 

def load_df():
    with open('data/data_sample_reduced', "rb") as fh:
        df = pickle.load(fh)
    return df


def load_gmm():
    gmm_name = 'data/gmm_29_04_21'
    means = np.load(gmm_name + '_means.npy')
    covar = np.load(gmm_name + '_covariances.npy')
    gmm = mixture.GaussianMixture(n_components = len(means), covariance_type='full')
    gmm.precisions_cholesky_ = np.linalg.cholesky(np.linalg.inv(covar))
    gmm.weights_ = np.load(gmm_name + '_weights.npy')
    gmm.means_ = means
    gmm.covariances_ = covar
    return gmm


def load_station():
    with open('data/stations_lat_utm.pkl', "rb") as fh:
        stations = pickle.load(fh)
    return np.array(stations)

#@st.cache
def load_sg():
    with open('data/sg.pkl', "rb") as f:
        sg = pickle.load(f)
    return sg

#@st.cache
def load_nodes():
    with open('data/nodes.pkl', "rb") as f:
        nodes = pickle.load(f)
    return nodes
    
def load_LR():
    with open('data/LR.pkl', "rb") as f:
        LR = pickle.load(f)
    return LR
def make_document(doc):       
    lat_london, long_london = 51.5073509, -0.1277583
    lon, lat = cp.wgs84_to_web_mercator(lat_london, long_london)

    source = ColumnDataSource(pd.DataFrame({'x_utm':[lon], 'y_utm':[lat]}))

    df = load_df()
    gmm_name = 'data/gmm_29_04_21'
    gmm = load_gmm()
    station_names = np.load(gmm_name + '_stations.npy')
    station_coord = load_station()

    #sg = load_sg()
    #nodes = load_nodes()
    LR = load_LR()
    tuile = get_provider('STAMEN_TERRAIN_RETINA')
    tuile2 = get_provider('STAMEN_TERRAIN_RETINA')
    fake_source = ColumnDataSource(pd.DataFrame({'x':[-1000], 'y':[-1000]}))
    # On récupère les valeurs mini/maxi des coordonnées,
    # on rajoute 10km pour avoir une carte centrée
    xutm_min, xutm_max, yutm_min, yutm_max = -66683.10992827898, 44365.159477674686, 6662336.264726096, 6754479.754163451

    x_range, y_range, x_axis_type, y_axis_type = (xutm_min, xutm_max), (yutm_min, yutm_max), 'mercator', 'mercator'

    p = figure(x_range=x_range, y_range=y_range, tools='tap, box_zoom, reset', plot_width=800, plot_height=800)
    p.add_tile(tuile)
    text_row = TextInput(value = None, title = "Custom output:", width = 420)

    circled = p.circle(x='x_utm',y='y_utm', size=10, fill_color='red', line_color='red', source=source)

    selected_stations = ColumnDataSource(pd.DataFrame({'x_utm':[], 'y_utm':[]}))
    selected_paths = ColumnDataSource(pd.DataFrame({'x':[], 'y':[]}))
    circled_stations = p.circle(x='x_utm',y='y_utm', size=10, source=selected_stations)
    paths_stations = p.line(x='x',y='y', line_color='blue', source=selected_paths)
    p.border_fill_color  = "#f0f0f5"
    p.xaxis.axis_label = 'Lon'
    p.yaxis.axis_label = 'Lat'
    p.title.text = "Clic anywhere to start moving the point. \n Clic again to select position"
    p.title.align = "center"
    p.title.text_color = "black"
    p.title.text_font_size = "20px"

    table_data = pd.DataFrame({'Station':[], 'Distance (m)':[], 'Temps prédit':[], 'Classement':[]})
    table_source = ColumnDataSource(table_data)
    template="""
    <div style="font-size: 20px;">
    <%= value %>
    </div>
    """
    fmt = HTMLTemplateFormatter(template=template)
    columns = [TableColumn(field=C, title=C, formatter =fmt) for C in table_data.columns]
    data_table = DataTable(source=table_source, columns=columns, width=800, height=800)
    style = Div(text="""
        <style>
        .my-table 
        .grid-canvas {
            background: #f0f0f5;
        }
        .slick-header-column:nth-child(3) 
        .slick-column-name{
        margin-bottom: 0px;
        } 
        .slick-header-column.ui-state-default {
            position: relative;
            color: black;
            font-size: 20px;
        }
            </style>
        """)
    def get_stations_data(c, dists):
        station, temps, cl,  conf = [], [], [], []
        for i, sta in enumerate(c):
            pred = LR[sta].predict(np.array(dists[i]).reshape(1, -1))
            station.append(station_names[sta])
            temps.append(np.round(pred, 2))
        cl = [sorted(temps).index(x) for x in temps]
        return {'Station':station, 'Distance (m)':dists, 'Temps prédit':temps, 'Classement':cl}

    is_taped = False
    def on_mouse_tap(event):
        global is_taped
        if is_taped:
            is_taped = False
        else:
            is_taped = True
        
    def on_mouse_mv(event):
        if is_taped:
            circled.data_source.data['x_utm'] = [event.x]
            circled.data_source.data['y_utm'] = [event.y]
            stations_select, line_x, line_y, dists = get_stations_new(event.x, event.y)
            prediction = get_stations_data(stations_select, dists)
            circled_stations.data_source.data = {'x_utm':station_coord[stations_select, 2], 'y_utm':station_coord[stations_select, 3]}
            paths_stations.data_source.data = {'x':line_x, 'y':line_y}
            data_table.source.data = prediction
            data_table.update()
            text_row.value = str(event.x) + ' ' + str(event.y)

    p.on_event(Tap, on_mouse_tap)
    p.on_event(MouseMove, on_mouse_mv)

    #plots = layout([p, Column(data_table, style)], [text_row])
    plots = layout([[p, Column(data_table, style)]])
    doc.title('London Fever : Outil de prédiction')
    doc.add_root(plots)
    
 
def exec_bok_serv():
    apps = {'/': Application(FunctionHandler(make_document))}
    server = Server(apps, port=5000)
    server.start()