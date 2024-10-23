"""Streamlit app"""
import streamlit as st

# Title of the app
st.title('Greeting Streamlit')

# Sidebar options for language and gender
language = st.sidebar.selectbox('Language:', ['English', 'French'])
gender = st.sidebar.selectbox('Gender:', ['Man', 'Woman'])

# Input field to ask for the person's name
name = st.text_input('Please enter your name:')

# Logic to display the greeting based on the selected language and gender
if name:
    if language == 'English' and gender == 'Man':
        st.write(f"Hello Mr. {name}")
    elif language == 'English' and gender == 'Woman':
        st.write(f"Hello Ms. {name}")
    elif language == 'French' and gender == 'Man':
        st.write(f"Bonjour monsieur {name}")
    elif language == 'French' and gender == 'Woman':
        st.write(f"Bonjour madame {name}")
