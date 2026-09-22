"""Anthropic provider for Cortex CLI."""

import os
from typing import Optional

import requests

from ai_cli.providers.base import BaseProvider
from ai_cli.config import get_api_key


class AnthropicProvider(BaseProvider):
    def __init__(self, model: Optional[str] = None, api_key: Optional[str] = None, **kwargs):
        super().__init__(model=model, **kwargs)
        self.api_key = api_key or get_api_key("anthropic") or os.environ.get("ANTHROPIC_API_KEY")
        self.base_url = kwargs.get("base_url", "https://api.anthropic.com/v1")

    def generate(self, prompt: str) -> str:
        if not self.api_key:
            raise ValueError("Anthropic API key not configured")
        response = requests.post(
            f"{self.base_url}/messages",
            headers={
                "x-api-key": self.api_key,
                "Content-Type": "application/json",
                "anthropic-version": "2023-06-01",
            },
            json={
                "model": self.model or "claude-3-opus-20240229",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": prompt}],
            },
        )
        response.raise_for_status()
        data = response.json()
        return data["content"][0]["text"]

    def list_models(self) -> list:
        return ["claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240924"]

    def is_available(self) -> bool:
        return bool(self.api_key) and self.api_key.startswith("sk-ant-")

    def __repr__(self):
        return f"AnthropicProvider(model={self.model}, key_set={bool(self.api_key)})"
