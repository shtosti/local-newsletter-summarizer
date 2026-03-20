import json
import os


class SafeDict(dict):
    def __missing__(self, key):
        return "{" + key + "}"


class PromptManager:
    def __init__(self, prompts_file):
        self.prompts_file = prompts_file
        self.shared_prefix = ""
        self.prompts = {}
        self._load()

    def _load(self):
        if not os.path.exists(self.prompts_file):
            raise FileNotFoundError(f"Prompt file not found: {self.prompts_file}")

        with open(self.prompts_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.shared_prefix = (data.get("shared_prefix") or "").strip()
        self.prompts = data.get("prompts") or {}

    def get_prompt(self, key, variables=None, fallback=None):
        template = self.prompts.get(key) or fallback or "Create a concise markdown summary:"
        variables = variables or {}
        rendered_template = template.format_map(SafeDict(variables)).strip()

        if self.shared_prefix:
            return f"{self.shared_prefix}\n\n{rendered_template}".strip()

        return rendered_template
