from app.services.Agent import Agent
from app.services.LLMManager import LLMManager
from app.services.TopicManager import TopicManager
import os

def buildAgent():
    llm = LLMManager(apiKey = os.getenv('OPENROUTER_API_KEY'),
                     model = "google/gemini-2.0-flash-lite-preview-02-05:free")
    agent = Agent(llm = llm)
    return agent
