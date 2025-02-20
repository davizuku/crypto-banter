import random

class PersonalityManager:
    def __init__(self):
        # TODO: obtain information from extracted data, maybe weighted on relevance
        self.styles = ["analytical", "reflective", "technical", "objective"]
        self.tones = ["positive", "enthusiastic", "intense", "irony", "pessimistic"]

    def getStyle(self) -> str:
        # TODO: add logic to choose styles
        return ', '.join(random.choices(self.styles, k=2))

    def getTone(self, topic: str) -> str:
        # TODO: add logic to choose tone
        return ', '.join(random.choices(self.tones, k=2))
