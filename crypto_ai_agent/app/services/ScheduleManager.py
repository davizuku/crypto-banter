from datetime import datetime, timedelta
import random

class ScheduleManager:
    def __init__(self):
        # TODO: obtain information from extracted data
        self.pastPosts = [
            { "topic": "Ethereum", "channel": "twitter", "date": datetime(2025, 1, 15, 14, 45, 30)},
            { "topic": "DeFi", "channel": "instagram", "date": datetime(2025, 2, 3, 9, 12, 45)},
            { "topic": "Layer 2", "channel": "twitter", "date": datetime(2025, 1, 25, 16, 30, 0)},
            { "topic": "Ethereum", "channel": "tiktok", "date": datetime(2025, 2, 10, 11, 5, 15)},
            { "topic": "Privacy", "channel": "twitter", "date": datetime(2025, 1, 20, 8, 55, 50)},
        ]

    def getDate(self, channel, topic) -> str:
        # TODO: add logic to choose date
        random_time = random.randint(1, 60 * 24 * 7)  # Random time between 1 minute and 7 days
        return datetime.now() + timedelta(minutes=random_time)
