"""Local model provider for Cortex CLI."""

import os
from typing import Optional

from ai_cli.providers.base import BaseProvider
from ai_cli.config import get_api_key


class LocalProvider(BaseProvider):
    def __init__(self, model: Optional[str] = None, endpoint: Optional[str] = None, **kwargs):
        super().__init__(model=model, **kwargs)
        self.endpoint = endpoint or os.environ.get("CORTEX_BASE_URL", "http://localhost:11434")

    def generate(self, prompt: str) -> str:
        import requests
        response = requests.post(
            f"{self.endpoint}/api/generate",
            json={
                "model": self.model or "llama3",
                "prompt": prompt,
                "stream": False,
            },
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")

    def list_models(self) -> list:
        import requests
        try:
            response = requests.get(f"{self.endpoint}/api/tags")
            response.raise_for_status()
            models = response.json().get("models", [])
            return [m["name"] for m in models]
        except Exception:
            return ["llama3", "mistral", "phi3"]

    def is_available(self) -> bool:
        import requests
        try:
            response = requests.get(f"{self.endpoint}/api/tags", timeout=2)
            return response.status_code == 200
        except Exception:
            return False

    def __repr__(self):
        return f"LocalProvider(endpoint={self.endpoint}, model={self.model})"
