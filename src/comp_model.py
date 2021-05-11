import streamlit as st
import numpy as np
import pandas as pd

from bokeh.plotting import figure
from bokeh.io import  push_notebook,output_notebook, show
from bokeh.models import ColumnDataSource, LabelSet,Ellipse, Column
from bokeh.models import CustomJS, Slider
from bokeh.tile_providers import get_provider
from bokeh.layouts import row, layout, column, widgetbox
import pickle as pickle 

def load_ellipses():
    with open('data/dico_gm', "rb") as fh:
        dico_gm = pickle.load(fh)
    with open('data/res_gm', "rb") as fh:
     res_g = pickle.load(fh)

    return dico_gm, res_g
    
def load_k():
    with open('data/dico_km', "rb") as fh:
        dico_km = pickle.load(fh)
    with open('data/res_km', "rb") as fh:
     res_k = pickle.load(fh)
    return dico_km, res_k
    
def make_figure():
    dico_gm, res_gm = load_ellipses()
    dico_km, res_k = load_k()
    labs = []
    x1, y1 = -586.6787726901897, 6748974.302499981 #bok_point
    x2, y2 = -586.6787726901897, 6740986.345180229 #bok_point
    for i, j in zip(res_gm, res_k):
        labs.append({'x':[x1, x2],
                    'y':[y1, y2],
                    'text':['GMM score : '+str(np.round(i, 2)),
                            'KM  score : '+str(np.round(j, 2))],
                    'text_color':['blue','red']})
                            
    tuile = get_provider('CARTODBPOSITRON_RETINA')
    xutm_min, xutm_max, yutm_min, yutm_max = -66683.10992827898, 44365.159477674686, 6662336.264726096, 6754479.754163451
    x_range, y_range, x_axis_type, y_axis_type = (xutm_min, xutm_max), (yutm_min, yutm_max), 'mercator', 'mercator'
    p = figure(x_range=x_range, 
               y_range=y_range, 
               x_axis_type=x_axis_type, 
               y_axis_type=y_axis_type,
               toolbar_location=None,
               plot_width=600,
               plot_height=600)
    p.add_tile(tuile)
    p.border_fill_color  = "#f0f0f5"
    station_ = p.circle(x='x',
                        y='y', 
                        size=5, 
                        fill_color='blue', 
                        source=ColumnDataSource(dico_gm[0]))
    station_km = p.circle(x='x',
                          y='y', 
                          size=5,
                          fill_color='red', 
                          line_color='red',
                          source=ColumnDataSource(dico_km[0]))
    ellipses = p.ellipse(x='x', 
                         y='y', 
                         width='width', 
                         height='height', 
                         angle='angle', 
                         fill_color="#cab2d6", 
                         fill_alpha=0.1,
                         source=ColumnDataSource(dico_gm[0]))
    labels = LabelSet(x='x',
                      y='y', 
                      text='text',
                      text_color='text_color',
                      x_offset=5, 
                      y_offset=5, 
                      source=ColumnDataSource(labs[0]), 
                      render_mode='canvas')
    p.add_layout(labels)
    slider = Slider(title='Distance du point de départ (%)',
                value=0,
                start=0,
                end=100,
                show_value=False,
                step=10)
    slider_callback = CustomJS(
    args=dict(station_km = station_km,
              dico_km = dico_km,
              ellipses = ellipses,
              dico_gm = dico_gm,
              labels = labels,
              labs = labs), code="""
        var value = cb_obj.value;
        var index = ~~(value/10)
        station_km.data_source.data = dico_km[index];
        station_km.data_source.change.emit();
        ellipses.data_source.data = dico_gm[index];
        ellipses.data_source.change.emit();
        labels.source.data = labs[index];
        labels.source.data.change.emit();
    """)
    slider.js_on_change('value', slider_callback)
    layout = column(slider, p)
    st.bokeh_chart(layout, use_container_width=False)
    
def description():
    
    st.markdown('''Si l'on veut pouvoir prédire combien de temps une station mettrait à se rendre à un point sur la carte
    nous avons plusieures options :''')
    with st.beta_expander("- Sélectionner toutes les stations dans un périmètre fixé"):
        st.markdown('''La sélection de station pourrait être source d'erreur. En effet, les stations du centre de Londre 
                    n'ont peut-être pas le même périmètre d'intervention que les stations en périphérie. En outre, 
                    plusieurs critères nous sont inconnus et devrait pondérer cette sélection : les voies rapides,
                    les itinéraires préférés, la topologie, etc...''')
    with st.beta_expander("- Classifier des coordonnées avec les stations en label"):
        st.markdown('''En revanche, si l'on base la classification des données sur l'historique des interventions, 
                    le modèle devrait capturer de nombreuses caractéristiques vis-à-vis du déplacement des pompiers,
                    et donc renvoyer quelle station devrait intervenir sur untel point.''')                
    st.markdown('''**K moyens**  
    Généralement, on approche ce type de classification avec les K moyens :
    On cherche alors à attribuer à chaque coordonnées d'incident, un centre qui correspondrait un à une station.  
    Le principal inconvénient est que les stations ont pu intervénir à des distances très variables.
    Comme on peut le voir sur le graphique intéractif, les K moyens ont un score de départ moyens (45 % de réussite),
    et uniquement lorsque les données sont entraînées avec une destination tronquée (portion de la distance station-incident).  
    **Mixtures Gaussiennes**  
    Les Mixtures Gaussiennes (*Gaussian Mixture Model*, GMM) sont une généralisation des K moyens :  
    En plus des coordonnées des centres, le modèle va estimer une covariance pour chacune des stations.  
    On obtient alors pour chaque point la probabilité "d'appartenir" à chaque station.
    On peut alors contrôler, parmis les stations prédites, si la station qui est effectivement intervenu est présente.  
    On peut également proposer quelles autres stations alentours seraient disposées à intervenir !  
    ''')

def write_page_FR():
    s1 = """
        <div style="text-align: center; font-size: 25px"> <b> Quelles Stations sont susceptibles d'intervenir sur un lieu d'incident ? <br><br>
        </div>
        """
    st.markdown(s1, unsafe_allow_html=True)
    cols = st.beta_columns((1, 1))
    with cols[0]:
        hide_full_screen = '''
        <style>
        .element-container:nth-child(3) .overlayBtn {visibility: hidden;}
        .element-container:nth-child(12) .overlayBtn {visibility: hidden;}
        </style>
        '''
        st.markdown(hide_full_screen, unsafe_allow_html=True) 
        make_figure()
    with cols[1]:
        description()
    s2 = """
    <div style="text-align: center"> <b> On peut voir en faisant varier le graphique, que le GMM est plus performant avec les données non-tronquées <br>
    Ce modèle est plus approprié pour trouver quelles stations seraient susceptibles d'intervenir.
    </div>
    """
    st.markdown(s2, unsafe_allow_html=True)
    
def description2():
    
    st.markdown('''If we want to be able to predict how much time a station would take to get to a point on the map we have several options :''')
    with st.beta_expander("- Select all stations within a fixed perimeter"):
        st.markdown('''The station selection could be a source of error. Indeed, the stations of London's center may not have the same range of intervention as the stations on the outskirts. In addition, several criteria are unknown to us and could influence this selection: expressways, preferred routes, topology, etc ...''')
    with st.beta_expander("- Classify coordinates with stations as labels"):
        st.markdown('''On the other hand, if the classification of the data is based on the history of interventions, the model should capture many characteristics with respect to the movement of firefighters, and therefore return which station should intervene on a certain location.''')                
    st.markdown('''**K means**  
    Typically, we approach this kind of classification with K means models: we then try to attribute to each incident coordinates a center which would correspond to an intervening station.
    The main drawback is that the stations were able to intervene at widely varying distances.
    As  we can see on the interactive graph, the K means have an average score (45% success), 
    and only when the data is trained with a truncated destination (portion of the station-incident distance).''')
    st.markdown('''** Gaussian mixtures**
    The *Gaussian Mixture Model* (GMM) are a generalization of the K means: In addition to the coordinates of the centers, the model will estimate a covariance for each of the stations.
    We then obtain for each point the probability of "belonging" to each station.
    It is then possible to check, among the predicted stations, whether the station which actually intervened is present.
    We can also suggest which other nearby stations would be willing to intervene!  
    ''')
def write_page_ENG():
    s1 = """
        <div style="text-align: center; font-size: 25px"> <b> Which Stations are most likely to intervene on an incident ? <br><br>
        </div>
        """
    st.markdown(s1, unsafe_allow_html=True)
    cols = st.beta_columns((1, 1))
    with cols[0]:
        hide_full_screen = '''
        <style>
        .element-container:nth-child(3) .overlayBtn {visibility: hidden;}
        .element-container:nth-child(12) .overlayBtn {visibility: hidden;}
        </style>
        '''
        st.markdown(hide_full_screen, unsafe_allow_html=True) 
        make_figure()
    with cols[1]:
        description2()
    s2 = """
    <div style="text-align: center"> <b> We can see when we modify the graph that the Gaussian Mixture Model is more efficient with non-truncated data <br>
     This model appears more suitable for identifying which stations would be likely to intervene.
    </div>
    """
    st.markdown(s2, unsafe_allow_html=True)