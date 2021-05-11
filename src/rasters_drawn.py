import streamlit.components.v1 as components
import streamlit as st

@st.cache(max_entries=20, ttl=360)
def image1():
    Htmldist = open("figures/rasters.html", 'r', encoding='utf-8')
    source_code1 = Htmldist.read()
    return source_code1

def write_page_FR():
    s_t = """
    <div style="text-align: center; font-size: 25px"> <b> Outil de visualisation des statistiques de chaque station<br><br>
    </div>
    """
    s_1 = """
    <div style="font-size: 15px"> Cet outil permet de visualiser l'emplacement de chacun des stations (après 2016).<br>
    En cliquand sur le graphique en haut à gauche ou la table en bas à gauche, vous pourrez visualiser les lieux d'incidents,
    ainsi que les statistiques globale de la station sélectionnée.<br>
    La station séléctionnée sera également affichée avec la covariance du noyau GMM associé.<br>
    Cliquez ailleurs sur la carte de gauche pour réinitialiser les données.
    </div>
    """
    st.markdown(s_t, unsafe_allow_html=True)
    st.markdown(s_1, unsafe_allow_html=True)
    components.html(image1(), height = 1200)
    
def write_page_ENG():
    s_t = """
    <div style="text-align: center; font-size: 25px"> <b> Statistics visualization tool for each station<br><br>
    </div>
    """
    s_1 = """
    <div style="font-size: 15px"> This tool allows you to view the location of each station (after 2016).<br>
    By clicking on the graph at the top left or the table at the bottom left, you will be able to view the location of incidents, as well as the overall statistics of the selected station. <br>
    The selected station will also be displayed with the associated GMM core covariance. <br>
    Click elsewhere on the left card to reset the data.
    </div>
    """
    st.markdown(s_t, unsafe_allow_html=True)
    st.markdown(s_1, unsafe_allow_html=True)
    components.html(image1(), height = 1200)