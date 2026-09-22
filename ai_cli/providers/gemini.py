"""Gemini provider for Cortex CLI."""

import os
from typing import Optional

import requests

from ai_cli.providers.base import BaseProvider
from ai_cli.config import get_api_key


class GeminiProvider(BaseProvider):
    def __init__(self, model: Optional[str] = None, api_key: Optional[str] = None, **kwargs):
        super().__init__(model=model, **kwargs)
        self.api_key = api_key or get_api_key("gemini") or os.environ.get("GEMINI_API_KEY")
        self.base_url = kwargs.get("base_url", "https://generativelanguage.googleapis.com/v1beta")

    def generate(self, prompt: str) -> str:
        if not self.api_key:
            raise ValueError("Gemini API key not configured")
        response = requests.post(
            f"{self.base_url}/models/{self.model or 'gemini-3.6-flash'}:generateContent",
            params={"key": self.api_key},
            json={
                "contents": [{"parts": [{"text": prompt}]}],
            },
        )
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]

    def list_models(self) -> list:
        return [
            "gemini-3.6-flash",
            "gemini-2.0-flash",
            "gemini-1.5-pro",
            "gemini-1.5-flash",
            "gemini-1.5-flash-8b",
        ]

    def is_available(self) -> bool:
        return bool(self.api_key) and len(self.api_key) > 10

    def __repr__(self):
        return f"GeminiProvider(model={self.model}, key_set={bool(self.api_key)})"
