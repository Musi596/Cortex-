"""Groq provider for Cortex CLI."""

import os
from typing import Optional

import requests

from ai_cli.providers.base import BaseProvider
from ai_cli.config import get_api_key


class GroqProvider(BaseProvider):
    def __init__(self, model: Optional[str] = None, api_key: Optional[str] = None, **kwargs):
        super().__init__(model=model, **kwargs)
        self.api_key = api_key or get_api_key("groq") or os.environ.get("GROQ_API_KEY")
        self.base_url = kwargs.get("base_url", "https://api.groq.com/openai/v1")

    def generate(self, prompt: str) -> str:
        if not self.api_key:
            raise ValueError("Groq API key not configured")
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.model or "llama-3.3-70b-versatile",
                "messages": [{"role": "user", "content": prompt}],
            },
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]

    def list_models(self) -> list:
        return [
            "llama-3.3-70b-versatile",
            "llama-3.1-70b-versatile",
            "llama-3.1-8b-instant",
            "mixtral-8x7b-32768",
            "gemma-7b-it",
        ]

    def is_available(self) -> bool:
        return bool(self.api_key) and len(self.api_key) > 10

    def __repr__(self):
        return f"GroqProvider(model={self.model}, key_set={bool(self.api_key)})"
