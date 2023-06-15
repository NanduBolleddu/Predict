import streamlit as st
import pickle 
import numpy as np
import time

def show_about():
    #linkedin
    st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">', unsafe_allow_html=True)
    #gmail
    st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">', unsafe_allow_html=True)

    
    with open('styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

    image_path = "1.jpg" 
    description = "This is an example image."
    st.subheader("Team Guide")
    col1, col2 = st.columns([1,3])
    col1.image(image_path, use_column_width=True)
    with col2:
        st.text('''
            V. Surya Narayana Reddy
            Department of CSE -(Cys,DS) and AI&DS
        ''')
        x1,x2,x3,x4,x5,x6,x7,x8,x9,x10 = st.columns(10)
        x1.markdown(f'<a href="{"https://www.linkedin.com/in/nanda-kishore-babu-bolleddu/"}"><i class="fab fa-linkedin"></i></a>', unsafe_allow_html=True)
        x2.markdown(f'<a href="mailto:{"veeramreddysurya@gmail.com"}"><i class="far fa-envelope"></i></a>', unsafe_allow_html=True)

    st.divider()
    st.subheader("Team Members")
    c1,c2,c3 = st.columns(3)
    with c1:
        c1.image(image_path, use_column_width=True)
        c1.text("Nanda Kishore Babu")
        x1,x2,x3,x4,x5,x6,x7 = st.columns(7)
        x1.markdown(f'<a href="{"https://www.linkedin.com/in/nanda-kishore-babu-bolleddu/"}"><i class="fab fa-linkedin"></i></a>', unsafe_allow_html=True)
        x2.markdown(f'<a href="mailto:{"nandakishore788130@gmail.com"}"><i class="far fa-envelope"></i></a>', unsafe_allow_html=True)
    with c2:
        c2.image(image_path, use_column_width=True)
        c2.text("Sharath Reddy")
        x1,x2,x3,x4,x5,x6,x7 = st.columns(7)
        x1.markdown(f'<a href="{"https://www.linkedin.com/in/sharath-reddy-jakkidi/"}"><i class="fab fa-linkedin"></i></a>', unsafe_allow_html=True)
        x2.markdown(f'<a href="mailto:{"j.sharathreddy123@gmail.com"}"><i class="far fa-envelope"></i></a>', unsafe_allow_html=True)
    with c3:
        c3.image(image_path, use_column_width=True)
        c3.text("J S Rithvik")
        x1,x2,x3,x4,x5,x6,x7 = st.columns(7)
        x1.markdown(f'<a href="{"https://www.linkedin.com/in/rithvik-rithvik-75233526a"}"><i class="fab fa-linkedin"></i></a>', unsafe_allow_html=True)
        x2.markdown(f'<a href="mailto:{"rithvikrithvik20@gmail.com"}"><i class="far fa-envelope"></i></a>', unsafe_allow_html=True)
