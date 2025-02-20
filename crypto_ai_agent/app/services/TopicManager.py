import random

class TopicManager:
    def __init__(self):
        # TODO: obtain topics from extracted data, maybe weighted on relevance
        self.topics = ["Ethereum", "DeFi", "Layer 2", "Privacy", "Decentralization"]

    def getTopic(self):
        # TODO: choose topic based on history of topics and news
        return random.choice(self.topics)
