import streamlit as st
import base64

#@st.cache(suppress_st_warning=True) 
def write_page_FR():
    pdf_file = 'doc/Projet_LFB_London_Fever_FR.pdf'
    with open(pdf_file,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1000" type="application/pdf">' 
        st.markdown(pdf_display, unsafe_allow_html=True)
        
        