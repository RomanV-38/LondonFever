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
    