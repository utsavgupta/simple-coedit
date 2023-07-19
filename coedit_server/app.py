#!/usr/bin/env python -tt

from flask import Flask
from flask import request
from flask_cors import CORS

from transformers import AutoTokenizer, T5ForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")
model = T5ForConditionalGeneration.from_pretrained("grammarly/coedit-large")

app = Flask(__name__)
CORS(app)

@app.route("/process", methods = ["POST"])
def process():

    body = request.get_json()
    transformation = body['transformation']
    text = body['text']
    input_text = transformation + ":" + text
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=256)
    decoded_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"transformed_text": decoded_text}