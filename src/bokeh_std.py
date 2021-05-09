import streamlit as st
import streamlit.components.v1 as components
def write_page():
    st.write("Cette page conduit à un serveur Bokeh, plus performant pour l'affichage de l'application de prédiction")
    #link = '[Bokeh Server](http://localhost:5000/)'
    #st.markdown(link, unsafe_allow_html=True)
    
    components.iframe("http://localhost:5006/bok_point_mousemove", height=1000)