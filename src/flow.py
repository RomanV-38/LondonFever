import streamlit as st 

def write_page_FR():
    s_t = """
    <div style="text-align: center; font-size: 25px"> <b> Illustration de la procédure de l'application finale (Onglet Outil de prédiction)
    </div>
    """
    description = '''
    <br><br><br><br><br><br>
    <div style="font: 15px"> <b> 
    Une fois le Dataset chargé </b>, on peut définir de nouvelles coordonnées (sur carte).  
    <br><br><br><br><br>
    <b>On utilise le modèle pré-entraîné de Mixture Gaussiennes (GMM)</b>, pour déterminer la 
    probabilité que cet incident soit attribué à chacune des stations.  
    <br><br><br><br>
    Ensuite, <b>on fixe un seuil</b> : dans notre cas, il est à 0.1%.
    Avec ce seuil, les stations sélectionnées contenaient la station indiquée par le Dataset dans 95% des cas.
    <br><br><br><br>
    
    <b>Pour chacune des stations sélectionnées</b>, on détermine la distance euclidienne entre la station et l'incident.
    Nous avons vu que pour notre Dataset, <b>la distance réellement parcourue est environ 75% de la distance euclidienne</b>
    calculée sur coordonnées UTM.
    
    <br>
    On peut alors <b>prédire le temps d'intervention</b>, en utilisant des régressions linéaire pré-entraînées pour chaque station.    
    </div>
    '''
    st.markdown(s_t, unsafe_allow_html=True)
    cols = st.beta_columns(2)
    with cols[0]:
        st.image('figures/flowchart.png')
    with cols[1]:
        st.markdown(description, unsafe_allow_html=True)
        
        
def write_page_ENG():
    s_t = """
    <div style="text-align: center; font-size: 25px"> <b> Illustrating the final application procedure (Prediction Tool tab)
    </div>
    """
    description = '''
    <br><br><br><br><br><br>
    <div style="font: 15px"> <b> 
    Once the Dataset is loaded </b>, we can select new coordinates (on the map).
    <br> <br> <br> <br> <br>
    <b> We use the pre-trained Gaussian Mixture Model  (GMM)</b>, to determine the
    probability that this incident is attributed to each of the stations.
    <br> <br> <br> <br>
    Then, <b> we set a threshold </b>: in our case, it is 0.1%.
    With this threshold, one of the stations selected matched the intervening station in the Dataset in 95% of cases.
    <br><br><br><br>
    
    <b> For each of the selected stations </b>, we calculate the Euclidean distance between the station and the incident.
    We observed that for our Dataset, <b> the distance traveled is about 75% of the Euclidean distance </b>
    calculated on UTM coordinates.
    
    <br>
    We can then <b> predict the response time </b>, using pre-trained linear regressions for each station.   
    </div>
    '''
    st.markdown(s_t, unsafe_allow_html=True)
    cols = st.beta_columns(2)
    with cols[0]:
        st.image('figures/flowchart.png')
    with cols[1]:
        st.markdown(description, unsafe_allow_html=True)