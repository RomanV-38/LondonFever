import streamlit as st
from PIL import Image

def write_page():
    s1 = """
        <div style="text-align: center; font-size: 25px"> <b> Analyse globale des temps d'intervention <br><br>
        </div>
        """
    s11 = """
        <div style=" font-size: 15px"> 
        On observe une forte variation des temps moyen d’intervention entre <b>10h et 21h</b>. <br>
        On peut logiquement la relier à une suractivité des unités de secours sur cette plage horaire 
        où la majorité de la population londonienne vaque à ses affaires.<br>
        On observe également une forte augmentation des temps d'intervention aux alentours de <b>4 heure du matin</b>. 
        On peut supposer que les interventions en plein milieu de la nuit demandent un temps de réaction plus important aux services de secours.
        </div>
        """
        
    s12 = """
        <div style=" font-size: 15px"> 
        L’évolution du temps moyen d’intervention par année présente également d’intéressantes variations. 
        On peut constater entre <b>2013</b> et <b>2016</b> une augmentation du temps d’intervention, avec une 
        chute importante en 2017 qui se <b>stabilise en dessous de 330 secondes</b>.<br>
        Il est très probable que ce phénomène traduise <b>les mesures de réorganisation de la 
        LFB</b> suite à la <b>réforme</b> engagée en <b>2013</b>. <br>
        Lors de cette réforme, la LFB a <b>fermé plusieurs 
        stations</b> de la métropole londonienne, ce qui suggère une évolution dans l'attribution des interventions.
        </div>
        """
    

    
    st.markdown(s1, unsafe_allow_html=True)
    cols2 = st.beta_columns(2)
    with cols2[0]:
        img = Image.open("figures/time_hour_line.png")
        st.image(img, width = 600, caption = "Temps d'intervention moyen (vert) et son écart type(bleu) par heures")
        st.markdown(s11, unsafe_allow_html=True)
        
    with cols2[1]:
        img = Image.open("figures/time_year_line.png")
        st.image(img, width = 600, caption = "Temps d'intervention moyen (vert) et son écart type(bleu) par années")
        st.markdown(s12, unsafe_allow_html=True)
    
    
    
    
    