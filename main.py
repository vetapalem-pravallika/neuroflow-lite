from fastapi import FastAPI
from agents import coordinator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "NeuroFlow API running"}

@app.post("/query")
def process_query(user_input: str):
    return coordinator(user_input)
