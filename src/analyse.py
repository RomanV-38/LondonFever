import streamlit as st
import comp_model
import presdataset
import fexp
import flow
import secexp
import trajets

def write_page():
    my_bar = st.progress(0)
    primaryColor = st.get_option("theme.primaryColor")
    s = """
    <style>
    div.stButton > button:first-child {
    background-color: #f0f0f5;color:black;font-size:20px;height:3em;width:10em;border-radius:10px 10px 10px 10px;
    }
    <\style>
    """
    st.markdown(s, unsafe_allow_html=True)
    cols = st.beta_columns(5)
    contains = st.beta_container()
    with cols[0]:
        if st.button("Dataset", key='button0'):
            with contains:
                presdataset.write_page()
                my_bar.progress(0.1)
    with cols[1]:
        if st.button("Analyse globale", key='button1'):
            with contains:
                my_bar.progress(0.2)
                fexp.write_page()
                secexp.write_page()
                
                
    with cols[2]:
        if st.button("Problématique", key='button2'):
            with contains:
                comp_model.write_page()
                my_bar.progress(0.4)
    with cols[3]:
        if st.button("Trajets", key='button3'):
            with contains:
                trajets.write_page()
                my_bar.progress(0.75)
    with cols[4]:
        if st.button("Algorithme", key='button4'):
            with contains:
                flow.write_page()
                my_bar.progress(1.0)
if __name__ == "__main__":
    write_page()