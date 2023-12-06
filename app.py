import streamlit as st
from main_page import main_page
from pneumonia_detection_page import pneumonia_detection_page
from creators import creators

# Set page title and favicon
st.set_page_config(page_title="Pneumonia Detection Website", page_icon=":microscope:", layout="wide")

# Logo and header
st.image("logo.png", width=220)
st.title("Pneumonia Detection Website")

# Menu
menu = ["Home", "Pneumonia Detection", "Creators"]
choice = st.sidebar.selectbox("Menu", menu)

# Define pages
if choice == "Home":
    main_page()

elif choice == "Pneumonia Detection":
    pneumonia_detection_page()

elif choice == "Creators":
    creators()


