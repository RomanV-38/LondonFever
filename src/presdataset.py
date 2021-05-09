import streamlit as st
import pandas as pd
import pickle as pickle

try : 
    with open('data/sample.pkl', "rb") as fh:
        df = pickle.load(fh)
except:
    import pickle5 as pickle
    with open('data/sample.pkl', "rb") as fh:
        df = pickle.load(fh)
def write_page():  
    s1 = """
        <div style="text-align: center; font-size: 25px"> <b> Présentation du jeu de données <br><br>
        </div>
        """
    s2 = """<div style="font-size: 15px">
        Les données mises à disposition par la <b>LFB</b> sont importantes : elles représentent 
        une fois fusionnées un peu moins de <b> 1 Go</b>. <br>
        Elles sont présentées sous la forme de <b>deux set</b> séparant les <b>mobilisations</b> et les <b>incidents</b>.
        Ces jeux de données sont composés de <b>2.032.480 évènements</b> couvrant toutes les 
        interventions des unités de secours depuis le <b>début de l'année 2009</b> jusqu'à la 
        fin du mois de <b>janvier 2021</b>. Les deux sets de données cumulent <b>75 colonnes individuelles</b>. <br>
        Nous avons de plus enrichis le jeu de données en ajoutant les <b>coordonnées géographiques </b>
        des stations, les coordonnées des interventions converties depuis le système britanniques,
        et les <b>distances euclidiennes</b> entre les stations intervenantes et les incidents.
        Après plusieurs décisions prises au cours de l'exploration et de la fusion des dataset,
        nous avons travaillé sur un jeu de données final de <b>1.797.003 entrées et 25 variables</b>.
        Ci-dessous, un extrait du jeu de données composé de lignes prélevées au hasard. <br>
        </div>
    """
        
    s3 = """<div style="font-size: 15px">
        Le jeu de données contient les coordonnées des interventions selon un système de coordonnées 
        géographiques cartésiennes. L'inconvénient est que le système de référence utilisé est le 
        <b>Ordnance Survey National Grid</b>, un référentiel datant de <b>1936 propre à la Grande-Bretagne</b> 
        qu'il nous faut projeter dans un référentiel universel. Pour les convertir en latitude et longitudes,
        nous avons eu recours à la bibliothèque python <b>convertbng</b>.<br>
        Les coordonnées des stations et des interventions postérieures à 2013 sont également disponible au format longitude/latitude. <br> 
        Pour calculer les distances, il nous a d'abord fallut les convertir en <b>Universal Transverse Mercator* (UTM)</b>.<br>
        Pour cela nous avons utilisé la formule suivante :<br>
        </div>
    """
    
    s4 = """<div style="font-size: 15px"> <br>
        Enfin, à partir des colonnes de <b>coordonnées en UTM</b> des stations et des incidents, 
        il a été possible de calculer la <b>distance euclidienne</b>, dans ce cas la distance à vol d'oiseaux, entre ces deux points.
        <br>
        La distance euclidienne a été calculée à partir de la formule suivante :
        <br>
        </div>
    """
    st.markdown(s1, unsafe_allow_html=True)
    st.dataframe(df)
    st.markdown(s2, unsafe_allow_html=True)
    with st.beta_expander("Pour en savoir plus sur le calcul des distances euclidiennes"):
            st.markdown(s3, unsafe_allow_html=True)
            st.latex(r'''x_{utm} = \text{lon} * (k * \frac{\pi}{180})''')
            st.write("\n\n")           
            st.latex(r'''y_{utm} = \log(\tan((90 + \text{lat}) * \frac{\pi}{360})) * k''')
            st.write(r'''où $k$ = 6378137, soit le rayon en mètres de la Terre.''')
            st.markdown(s4, unsafe_allow_html=True)
            st.latex(r'''dist_{ij} = \sqrt{(x_{i_{utm}} - x_{j_{utm}})^2 + (y_{i_{utm}} - y_{j_{utm}})^2}''')
            st.write("\n\n")
            st.write(r'''Pour $i, j$ chaque lieu d'incident et station de départ de l'intervention.''')          