from enum import auto
import streamlit as st
from PIL import Image

def app():
    st.title(" Derm-Care")
    st.write("")
    st.write("")
    st.subheader("Welcome to Derm Care")
    st.write("")
    st.write("")

    st.markdown("""---""")

    col1,col2,col3 = st.columns(3)

    col1.subheader("Click.")
    col1.text("Capture Infected Skin Image")
    col2.subheader("Upload.")
    col2.text("Upload Captured Image")
    col3.subheader("Predict.")
    col3.text("Get Predicted Result")
    st.markdown("""---""")  
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    show_file = st.empty()
    c1,c2,c3=st.columns([1,6,1])
    file = Image.open('Skin.jpg')
    c2.image(file, use_column_width=auto )

    st.markdown("""---""") 
    c1,c2,c3 = st.columns(3) 
    c1.text("Project By:")
    c1.text("Vedant Shirsekar")
    c1.text("18105A0021")
    c2.text("")
    c2.text("")
    c2.text("Soham Urunkar")
    c2.text("18105A0035")
    c3.text("")
    c3.text("")
    c3.text("Swarit Mahalsekar")
    c3.text("18105A0021")
    c3.text("")
    c3.text("")
    c3.text("")
    c3.text("")
    c3.text("")
    c3.text("")
    c3.text("")
    c3.text("")
    c3.text("your PROBLEM our SOLUTION")
