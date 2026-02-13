# Next Word Prediction System

An NLP application that predicts the most likely next word based on user input.  
Built with **FastAPI** for backend logic and **Streamlit** for the frontend, it leverages a pretrained **GPT‑2** model from Hugging Face Transformers.  
For deployment on Streamlit Cloud or Hugging Face Spaces, the app loads the model dynamically at runtime, avoiding large file uploads.

---

## Features
- Predicts the next word in real time.
- Interactive Streamlit interface for user input.
- Backend logic originally designed with FastAPI.
- Uses Hugging Face Transformers and PyTorch.
- Lightweight deployment: no large model files stored in the repo.

---

## How It Works
1. User enters text in the Streamlit interface.
2. The app encodes the input using the GPT‑2 tokenizer.
3. The GPT‑2 model generates predictions for the next word.
4. The result is displayed instantly in the UI.

---

## Project Structure
next_word_prediction/
  │── app.py   # Streamlit entry point
  │── backend.py     # Optional FastAPI backend 
  │── requirements.txt  # Dependencies
  │── README.md 
# Project documentation

---

## Requirements
- Python 3.8+
- Streamlit
- Transformers
- Torch

Install dependencies:
```bash
pip install
-r requirements.txt

## License
---

This README is structured, concise, and deployment‑ready. Do you want me to also add a **“Demo” section with screenshots or a Hugging Face/Streamlit Cloud link placeholder** so visitors can try it instantly once you deploy?
