from fastapi import FastAPI
from app.services.Factory import buildAgent

app = FastAPI()

agent = buildAgent()

@app.get("/generate")
def generate_post():
    post = agent.createPost()
    return post
