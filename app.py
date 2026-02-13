import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load model and tokenizer directly from Hugging Face Hub
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

st.title("Next Word Prediction System")

user_input = st.text_input("Enter text:")

if st.button("Predict Next Word"):
    inputs = tokenizer.encode(user_input, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=inputs.shape[1] + 1,
        do_sample=True,
        top_k=5
    )
    prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
    next_word = prediction.split()[-1]
    st.success(f"Predicted Next Word: {next_word}")