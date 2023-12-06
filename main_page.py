
import streamlit as st

def main_page():
    # st.title("Pneumonia Detection Website")

    st.write("""
    Welcome to the Pneumonia Detection Website! This website provides information on pneumonia detection based on chest X-rays. 
    
    Explore the available pages from the menu.
    """)

    

    st.header("What is Pneumonia?")
    st.write("""
    Pneumonia is an infection of one or both of the lungs caused by bacteria, viruses, or fungi. It is a serious infection in which the air sacs fill with pus and other liquid.
    """)

    st.header("How is Pneumonia Caused?")
    st.write("""
    Pneumonia is mostly spread when people infected cough, sneeze, or talk, sending respiratory droplets into the air. These droplets can then be inhaled by close contacts. Less often, you can get pneumonia from touching an object or surface that has the germ on it and then touching your nose or mouth.
    """)

    st.header("The Symptoms of Pneumonia:")
    st.write("""
    - Cough, which may produce greenish, yellow or even bloody mucus.
    - Fever, sweating, and shaking chills.
    - Shortness of breath.
    - Rapid, shallow breathing.
    - Sharp or stabbing chest pain that gets worse when you breathe deeply or cough.
    """)

    st.header("Is Pneumonia Serious?")
    st.write("""
    Pneumonia can be very serious and can cause death. Complications from pneumonia include respiratory failure, sepsis, and lung abscess and are more likely to affect older adults, young children, those with a weakened immune system, and people with other medical problems. Good health habits can fight pneumonia.
    """)

    st.header("How to Check Your Chest X-Ray for Pneumonia?")
    
    st.write("""
    Here is a simple demo on how you can check your chest X-ray to find out if you have pneumonia:
    """)
    st.video("demo.mp4")
    st.write("""
    Remember, it is essential to consult with a healthcare professional for a proper treatment if you are infected with Pneumonia .
    """)



if __name__ == "__main__":
    main_page()
