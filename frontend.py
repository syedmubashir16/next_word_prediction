import streamlit as st
import requests

st.title("Next Word Prediction System")

user_input = st.text_input("Enter text:")

if st.button("Predict Next Word"):
    response = requests.post("http://127.0.0.1:8000/predict", json={"text": user_input})
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Next Word: {result['next_word']}")
    else:
        st.error("Error connecting to backend")
