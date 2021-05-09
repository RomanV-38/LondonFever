import streamlit as st
import streamlit.components.v1 as components


def write_page():
    s1 = """
        <div style="text-align: center; font-size: 25px"> <br><br><b> Analyse globale du nombre et des distances d'intervention <br><br>
        </div>
        """
    s11  = """
        <div style="text-align: center; font-size: 20px"> 
        <b>Nombre d'intervention par station
        </div>
        """
    s111 = """
        <div style=" font-size: 15px">  
        On observe que les stations du centre de l’aire urbaine de Londres se démarquent 
        fortement des stations des périphéries. Le réseau des <b>stations centrales</b> apparaît
        également plus <b>concentré</b> dans cet espace, en adéquation avec sa <b>densité urbaine</b>. 
        Plus on s’éloigne du centre, et plus le taux d'intervention diminue. <br>
        Là aussi, il est très probable que la principale explication se 
        trouve dans la variation de la densité urbaine. 
       On remarque notamment les stations de <b>Soho</b>, avec plus de <b>58.000 </b>interventions, 
       et de <b>Paddington</b>, plus de <b>42.000</b>, en comparaisont des stations périphériques de
       <b>Wennington </b>ou <b>Biggin Hill</b> dont le nombre d'intervention avoisine <b>5.000</b>.   
        </div>
        """
    s12  = """
        <div style="text-align: center; font-size: 20px"> 
        <b>Distances moyennes parcourues par les stations
        </div>
        """ 
    s121 = """
        <div style=" font-size: 15px"> 
        La variation de la densité du réseau des stations peut également s’observer avec l’étude 
        des distances moyennes parcourues par les stations. Là aussi une différence entre le centre 
        et les périphérie est observable : Les stations du <b>centre</b> parcourent en effet en moyenne 
        <b>moins de distance</b> que les <b>stations des périphéries</b>. <br>
        En moyenne, les stations du <b>centre</b> parcourent environ <b>2.2km</b> dans
        leurs interventions, tandis que les stations en <b>périphérie</b> parcourent environ <b>4km</b>.
        </div>
        """
    


    
    st.markdown(s1, unsafe_allow_html=True)
    cols2 = st.beta_columns(2)
    with cols2[0]:
        Htmlinter = open("figures/inter.html", 'r', encoding='utf-8')
        source_code = Htmlinter.read()
        components.html(source_code, height = 600)
        st.markdown(s11, unsafe_allow_html=True)
        st.markdown(s111, unsafe_allow_html=True)
    with cols2[1]:
        Htmldist = open("figures/distmean.html", 'r', encoding='utf-8')
        source_code1 = Htmldist.read()
        components.html(source_code1, height = 600)
        st.markdown(s12, unsafe_allow_html=True)
        st.markdown(s121, unsafe_allow_html=True)
