import random
from typing import List

class MediaManager:
    def __init__(self):
        # TODO: obtain information from historical posts
        self.channels = ["twitter", "instagram", "tiktok", "blog"]
        self.maxWords = ["150", "100", "50", "1000"]

    def getChannel(self) -> List[str]:
        # TODO: add logic to choose styles
        index = random.randint(0, len(self.channels)-1)
        return self.channels[index], self.maxWords[index]
