from ollama import Client
from config import OLLAMA_MODEL, OLLAMA_HOST


class OllamaSummarizer:
    def __init__(self):
        self.client = Client(host=OLLAMA_HOST)
        self.model = OLLAMA_MODEL

    def summarize(self, texts, prompt="Create a concise markdown summary:"):
        combined_text = "\n\n".join(t for t in texts if t).strip()
        if not combined_text:
            return ""

        response = self.client.generate(
            model=self.model,
            prompt=f"{prompt}\n\n{combined_text}",
        )
        return response.get("response", "").strip()