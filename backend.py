from fastapi import FastAPI
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = FastAPI()

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict_next_word(input: InputText):
    inputs = tokenizer.encode(input.text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=inputs.shape[1]+1, do_sample=True, top_k=5)
    prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
    next_word = prediction.split()[-1]
    return {"next_word": next_word}
