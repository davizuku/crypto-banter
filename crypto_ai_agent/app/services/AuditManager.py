import random

class AuditManager:
    def __init__(self):
        # TODO: obtain information from extracted data
        self.trueSources = []

    def validate(self, post) -> str:
        # TODO: add logic to validate
        score = random.randint(0, 100)
        return score / 100.0
