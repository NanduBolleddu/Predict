import streamlit as st
import numpy as np
from prediction import show_prediction
from about import show_about


tab1, tab2 = st.tabs(["Predict","About"])
with tab1:
    data = show_prediction()
    if data == 0:
        st.subheader("Yeah!! Your Heart is Healthy..")
    elif data == 1:
        st.subheader("Consult a Doctor.")
        st.write("Follow the Link to Book an Appointment : [Link](https://hyderabad.apollohospitals.com/centers-of-excellence/heart/cardiologists-in-hyderabad/)")

with tab2:
    show_about()

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)



