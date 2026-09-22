"""OpenAI provider for Cortex CLI."""

import os
from typing import Optional

import requests

from ai_cli.providers.base import BaseProvider
from ai_cli.config import get_api_key


class OpenAIProvider(BaseProvider):
    def __init__(self, model: Optional[str] = None, api_key: Optional[str] = None, **kwargs):
        super().__init__(model=model, **kwargs)
        self.api_key = api_key or get_api_key("openai") or os.environ.get("OPENAI_API_KEY")
        self.base_url = kwargs.get("base_url", "https://api.openai.com/v1")

    def generate(self, prompt: str) -> str:
        if not self.api_key:
            raise ValueError("OpenAI API key not configured")
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.model or "gpt-4",
                "messages": [{"role": "user", "content": prompt}],
            },
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]

    def list_models(self) -> list:
        return ["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo", "gpt-4o", "gpt-4o-mini"]

    def is_available(self) -> bool:
        return bool(self.api_key) and len(self.api_key) > 20

    def __repr__(self):
        return f"OpenAIProvider(model={self.model}, key_set={bool(self.api_key)})"
