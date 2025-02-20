import requests
import json

class LLMManager:
    def __init__(self, apiKey: str, model: str = 'openai/gpt-4o-mini'):
        self.apiKey = apiKey
        self.model = model

    def complete(self, prompt: str) -> str:
        rawResponse = requests.post(
            url="https://openrouter.ai/api/v1/completions",
            headers={
                "Authorization": f"Bearer {self.apiKey}",
            },
            data=json.dumps({
                "model": self.model,
                "prompt": prompt
            })
        )
        response = json.loads(rawResponse.content)
        return response["choices"][0]["text"]
