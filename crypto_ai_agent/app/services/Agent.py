from app.services.TopicManager import TopicManager
from app.services.PersonalityManager import PersonalityManager
from app.services.MediaManager import MediaManager
from app.services.ScheduleManager import ScheduleManager
from app.services.AuditManager import AuditManager
from app.services.LLMManager import LLMManager

class Agent:
    def __init__(self,
                 topic: TopicManager,
                 personality: PersonalityManager,
                 media: MediaManager,
                 scheduler: ScheduleManager,
                 auditor: AuditManager,
                 llm: LLMManager):
        self.topic = topic
        self.personality = personality
        self.media = media
        self.scheduler = scheduler
        self.auditor = auditor
        self.llm = llm

    def createPost(self):
        # What to post?
        topic = self.topic.getTopic()
        # How to post?
        style = self.personality.getStyle()
        tone = self.personality.getTone(topic)
        # Where to post?
        channel, maxWords = self.media.getChannel()
        # When to post?
        date = self.scheduler.getDate(topic, channel)
        # Generate the post's text
        prompt = f"You are an expert community manager of a top voice in the crypto world.\
            Write a post for {channel} about {topic} using the style {style}. Keep your tone {tone}.\
            The post will be published on {date}, adapt the post to the date, if relevant.\
            Keep your post limited to at most {maxWords} words.\
            Return only the text of the post ready to copy-and-paste on the platform, do not add the date of the post."
        post = self.llm.complete(prompt=prompt)
        # TODO: generate image for the post using multi-modal model, if channel allows it.

        # Validate the veracity & reliability
        score = self.auditor.validate(post)

        # TODO: regenerate based on 'score'?

        return {
            "topic": topic,
            "personality": {
                "tone": tone,
                "style": style,
            },
            "media": {
                "channel": channel,
                "maxWords": maxWords,
            },
            "schedule": {
                "date": date
            },
            "post": post,
            "reliability": score,
        }
