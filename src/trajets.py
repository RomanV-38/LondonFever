import streamlit as st
import streamlit.components.v1 as components
base_ox = '''
nearestnode_origin, dist_o_to_onode = ox.distance.get_nearest_node(G, (o_lat, o_long), method='haversine', return_dist=True)
nearestnode_dest, dist_d_to_dnode = ox.distance.get_nearest_node(G, (d_lat, d_long), method='haversine', return_dist=True)

dist_to_network = dist_o_to_onode + dist_d_to_dnode
shortest_p = nx.shortest_path_length(G,
                                     nearestnode_origin, 
                                     nearestnode_dest,
                                     weight='length')'''
pbf_import = '''
# Initialise avec une bounding box
# Greater London pbf doit être récupéré sur le site OSM
from pyrosm import OSM, get_data
# Define a square around the origin node
# Or get the min-max of (origin_node, destination_node)
# Here x, y are lon, lat coordinates
north = origin_node_y+0.001
south = origin_node_y-0.001
east  = origin_node_x+0.001
west  = origin_node_x-0.001
osm = OSM(get_data("Greater London", directory="pbf_data"),
          bounding_box=[west, south, east, north])
nodes, edges = osm.get_network(network_type='driving', nodes=True)
G = osm.to_graph(nodes, edges, graph_type="networkx")'''

osm_import = '''
# Initialise avec une bounding box
# Le fichier OSM est trop important pour construire le graph en entier
# La fonction envoies une requête au serveur OSM
import osmnx as ox
# Get graph 20km around origin_node,
# here x, y are lon and lat coordinates
G = ox.graph_from_point((origin_node_lat, 
                         origin_node_lon), 
                         dist=20000, 
                         network_type='drive')'''
                         
shp_import = '''
# Initialise tout le graph
# Le fichier SHP doit être récupéré sur le site OSM
import networkx as nx
g = nx.read_shp('SHAPEFILE_REGION_OF_INTEREST.shp')
sgs = list(nx.connected_component_subgraphs(g.to_undirected()))
nodes, sg = cp.compute_nodes(sgs, dist_type='euclidean')'''

shp_traj = '''
pos0 = (origin_node_lat, origin_node_lon)
pos1 = (destination_node_lat, destination_node_lon)
# On identifie les noeuds les plus proches 
# des coordonnées origine et destination
pos0_i = np.argmin(
    np.sum((nodes[:, ::-1] - pos0)**2, axis=1))
pos1_i = np.argmin(
    np.sum((nodes[:, ::-1] - pos1)**2, axis=1))
# On calcule le trajet le plus court
length = nx.shortest_path_length(
    sg,
    source=tuple(nodes[pos0_i]),
    target=tuple(nodes[pos1_i]),
    weight='distance')'''
    
shp_comp = '''
import json		
def geocalc(lat0, lon0, lat1, lon1):
    EARTH_R = 6378137
    """Return the distance (in m) between two points
    in geographical coordinates."""
    lat0 = np.radians(lat0)
    lon0 = np.radians(lon0)
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    dlon = lon0 - lon1
    y = np.sqrt((np.cos(lat1) * np.sin(dlon)) ** 2 +
        (np.cos(lat0) * np.sin(lat1) - np.sin(lat0) *
         np.cos(lat1) * np.cos(dlon)) ** 2)
    x = np.sin(lat0) * np.sin(lat1) + \
        np.cos(lat0) * np.cos(lat1) * np.cos(dlon)
    c = np.arctan2(y, x)
    return EARTH_R * c
def wgs84_to_web_mercator(lat, lon):
    """
    from https://stackoverflow.com/questions/57178783/how-to-plot-latitude-and-longitude-in-bokeh
    Cette fonction calcule les coordonnées
    UTM (mercator) à partir de la longitude et de la latitude
    df : le dataframe où se trouvent les données à convertir
    lon : nom de la colonne pour les longitudes
    lat : nom de la colonne pour les latitudes
    return : retourne le dataframe en y ajoutant les colonnes 
    pour les coordonnées x_utm et y_utm
    """
    k = 6378137 # rayon de la Terre en mètres
    x = lon * (k * np.pi/180.0)
    y = np.log(np.tan((90 + lat) * np.pi/360.0)) * k
    return x, y
def distance_euclidean(lat0, lon0, lat1, lon1):
    x0, y0 = wgs84_to_web_mercator(lat0, lon0)
    x1, y1 = wgs84_to_web_mercator(lat1, lon1)
    return np.sqrt( (x0-x1)**2 + (y0-y1)**2)
	
def get_path_length(path):
    return np.sum(geocalc(path[1:, 1], path[1:, 0],
                          path[:-1, 1], path[:-1, 0]))
def get_path_length_euclidean(path):
    return np.sum(distance_euclidean(path[1:, 1], path[1:, 0],
                          path[:-1, 1], path[:-1, 0]))

def compute_nodes(sgs, dist_type='euclidean'):
    i = np.argmax([len(sg) for sg in sgs])
    sg = sgs[i]
    # Compute the length of the road segments.
    for n0, n1 in sg.edges:
        path = np.array(json.loads(sg[n0][n1]['Json'])['coordinates'])
        if dist_type == 'euclidean':
            distance = get_path_length_euclidean(path)
        elif dist_type == 'haversine':
            distance = get_path_length(path)
        else:
            print('dist_type doit être euclidean ou haversine')
        sg.edges[n0, n1]['distance'] = distance
    nodes = np.array(sg.nodes())
    return nodes, sg'''
def write_page():
    s_0 = """
    <div style="text-align: center; font-size: 25px"> <b> Calcul de trajets : les alternatives à la distance euclidienne <br><br>
    </div>
    """
    s_t = """
    <div style="text-align: center"> <b> Le calcul des trajets est une étape importante dans l'estimation des 
    distances que les pompiers doivent être amenés à parcourir. <br>
    Ces trajets peuvent être calculés de plusieures manières, décrites ci-dessous
    </div>
    """
    s_t2 = """
    <div style="text-align: center"> <b> Etant donné la comparaison des performances,
    Nous avons calculé les trajets station-incidents du Dataset avec la méthode PBF.
    </div>
    """
    st.markdown(s_0, unsafe_allow_html=True)
    st.markdown(s_t, unsafe_allow_html=True)
    cols = st.beta_columns(2)
    with cols[0]:
        st.image('figures/trajets.png')
        
    with cols[1]:
    
        st.write('La plus longue partie du calcul se situe dans la construction du Graph, à partir duquel on va estimer le trajet le plus court.')
        st.write('Une fois le Graph construit, on peut directement estimer la longueur du trajet avec NetworkX')
        with st.beta_expander('Méthode PBF'):
            st.code(pbf_import, language='python')
        with st.beta_expander('Méthode OSMNX'):
            st.code(osm_import, language='python')
        with st.beta_expander('Méthode SHP'):
            st.code(shp_import, language='python')
        with st.beta_expander('calcul trajet PBF et OSM'):
            st.code(base_ox, language='python')
        with st.beta_expander('calcul trajet SHP'):
            st.code(shp_traj, language='python')
    st.markdown(s_t2, unsafe_allow_html=True)
    
    with st.beta_expander('Fonctions utilitaires complémentaires pour SHP'):
        st.code(shp_comp, language='python')