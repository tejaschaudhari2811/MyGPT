import ollama
from typing import AnyStr

def get_response(question: AnyStr):
    response = ollama.chat(model="qwen2:0.5b", messages=[{
        "role":"user",
        "content" : f"{question}"
    }])
    return response["message"]["content"]