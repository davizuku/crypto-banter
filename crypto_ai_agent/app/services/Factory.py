from app.services.Agent import Agent
from app.services.TopicManager import TopicManager
from app.services.PersonalityManager import PersonalityManager
from app.services.MediaManager import MediaManager
from app.services.ScheduleManager import ScheduleManager
from app.services.AuditManager import AuditManager
from app.services.LLMManager import LLMManager
import os

def buildAgent():
    llm = LLMManager(apiKey = os.getenv('OPENROUTER_API_KEY'),
                     model = "google/gemini-2.0-flash-lite-preview-02-05:free")
    agent = Agent(
        topic = TopicManager(),
        personality = PersonalityManager(),
        media = MediaManager(),
        scheduler = ScheduleManager(),
        auditor = AuditManager(),
        llm = llm,
    )
    return agent
