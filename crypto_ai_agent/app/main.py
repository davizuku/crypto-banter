from fastapi import FastAPI
import requests
import json
import os

app = FastAPI()

@app.get("/generate")
def generate_post():
    prompt = "Say: 'Hello'"
    rawResponse = requests.post(
        url="https://openrouter.ai/api/v1/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        },
        data=json.dumps({
            "model": "google/gemini-2.0-flash-lite-preview-02-05:free",
            "prompt": prompt
        })
    )
    response = json.loads(rawResponse.content)
    return {
        "post": response["choices"][0]["text"]
    }

# Run with: uvicorn main:app --reload
