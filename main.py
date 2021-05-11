import streamlit as st
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'src'))
import bokeh_std
import pdf_reader
import intro
import analyse
import pickle
import rasters_drawn

PAGES = {
    "Introduction"             : intro,
    "Exploration des données"  : analyse,
    "Affichage dynamique"      : rasters_drawn,
    "PDF"                      : pdf_reader,
    "Outil de prédiction"      : bokeh_std,
    }

st.set_page_config(layout="wide")

def main():
    """Main function of the App"""
    lang = st.sidebar.selectbox('Language',
                         ('Français', 'English'))
                          
    if lang=='Français':
        st.sidebar.title("Navigation")
        selection = st.sidebar.radio("Go to", list(PAGES.keys()))
        page = PAGES[selection]
        page.write_page_FR()
        st.sidebar.title("Contribute")
        st.sidebar.info("London Fever : analyse des temps d'intervention de la LFB"
            "\n\n"
            "Participants:"
            "\n\n"
            "Roman VUILLAUME [linkedin](https://www.linkedin.com/in/Roman-Vuillaume)"
            "\n\n"
            "Charlie PARÉ [linkedin](https://www.linkedin.com/in/charlie-paré)"
            "\n\n"
            "Smail MAKOUDI [linkedin](https://fr.linkedin.com/in/smail-makoudi)"
            )
        st.sidebar.title("About")
        st.sidebar.info(
            "Projet de valiation de la formation Data Analyst - Promotion Bootcamp Mars 2021"
            "\n\n"
            "Réalisé sous la supervision de Greg TORDJMAN [linkedin](https://fr.linkedin.com/in/greg-tordjman)"
        )
    if lang=='English':
        st.sidebar.title("Navigation")
        selection = st.sidebar.radio("Go to", list(PAGES.keys()))
        page = PAGES[selection]
        page.write_page_ENG()
        st.sidebar.title("Contribute")
        st.sidebar.info("London Fever : analysing the LFB response time"
            "\n\n"
            "Participants:"
            "\n\n"
            "Roman VUILLAUME [linkedin](https://www.linkedin.com/in/Roman-Vuillaume)"
            "\n\n"
            "Charlie PARÉ [linkedin](https://www.linkedin.com/in/charlie-paré)"
            "\n\n"
            "Smail MAKOUDI [linkedin](https://fr.linkedin.com/in/smail-makoudi)"
            )
        st.sidebar.title("About")
        st.sidebar.info(
            "Data Analyst Bootcamp project - Mars 2021 session"
            "\n\n"
            "Realised with the supervision of Greg TORDJMAN [linkedin](https://fr.linkedin.com/in/greg-tordjman)"
        )

if __name__ == "__main__":
    #bok_point_mousemove.exec_bok_serv()
    main()