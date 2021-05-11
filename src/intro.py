import streamlit as st
from PIL import Image



def write_page_FR():
    s_title1 = """
    <div style="text-align: center; font-size: 40px;"> <b> London Fever </b> <br>
    </div>
    """
    s_title2 = """
    <div style="text-align: center; font-size: 25px;"> <b> Temps d'intervention des pompiers de Londres </b> <br>
    </div>
    """
    
    s_intro = """
    <div style="font-size: 17px;">
    La <b>London Fire Brigade</b> (LFB) et ses 102 stations interviennent sur les incidents dans toute l'aire urbaine de Londres.
    <br>
    Elle dénombre en moyenne un peu plus de <b>150.000 interventions</b> de natures diverses (incendies, secours aux personnes, etc.) par an.
    <br>
    Le temps d'intervention des forces de secours est l'un des facteurs majeurs dans la mitigation des dégâts aux personnes et matériels.
    <br>
    Pour cette raison, le maintien d'un temps d'intervention des premiers secours en dessous de <b>360 secondes</b> est l'un des principaux objectifs de la LFB.
    <br>
    Pour ce projet nous allons nous intéresser aux données de la LFB et proposer un modèle de prédiction capable de déterminer <b>le temps moyen d'intervention des stations environnantes</b>,
    à une adresse dans l'aire urbaine de Londres.
    </div>
    """
    
    cols = st.beta_columns(3)
    img = Image.open("figures/intro.png")
    with cols[1]:
        st.markdown(s_title1, unsafe_allow_html=True)
        st.markdown(s_title2, unsafe_allow_html=True)
        st.image(img, width = 500, caption = "")
    st.markdown(s_intro, unsafe_allow_html=True)


def write_page_ENG():
    s_title1 = """
    <div style="text-align: center; font-size: 40px;"> <b> London Fever </b> <br>
    </div>
    """
    s_title2 = """
    <div style="text-align: center; font-size: 25px;"> <b> London's rescue services response time </b> <br>
    </div>
    """
    
    s_intro = """
    <div style="font-size: 17px;">
    The <b>London Fire Brigade</b> (LFB) and it's 102 fire station provide rescue services all across the London urban area.
    <br>
    On average, the LFB mobilise a little over <b>150.000 times</b> per year, on incidents of diverse nature (fire, car-crash, etc)
    <br>
    The response time of rescue services is one of the major factors in mitigating damages to people and equipments.
    <br>
    For this reason, maintaining a first aid response time below <b> 360 seconds </b> is one of the main objectives of the LFB.
    <br>
    For this project we will take a look at the data displayed by the LFB and try to present a prediction model capable of determining <b> the average response time of surrounding stations </b>,
    to an address in the London urban area.
    </div>
    """
    
    cols = st.beta_columns(3)
    img = Image.open("figures/intro.png")
    with cols[1]:
        st.markdown(s_title1, unsafe_allow_html=True)
        st.markdown(s_title2, unsafe_allow_html=True)
        st.image(img, width = 500, caption = "")
    st.markdown(s_intro, unsafe_allow_html=True)