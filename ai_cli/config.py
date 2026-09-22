"""Configuration management for Cortex CLI."""

import os
from pathlib import Path
from typing import Optional

HOME = Path.home()
CONFIG_DIR = HOME / ".config" / "cortex"
CONFIG_FILE = CONFIG_DIR / "config.json"

SUPPORTED_PROVIDERS = [
    "openai",
    "anthropic",
    "gemini",
    "groq",
    "mercury",
    "local",
]

PROVIDER_KEY_PATTERNS = {
    "openai": lambda key: key.startswith("sk-") and not key.startswith("sk-ant-"),
    "anthropic": lambda key: key.startswith("sk-ant-"),
    "gemini": lambda key: key.startswith("AIza"),
    "groq": lambda key: key.startswith("gsk_"),
    "mercury": lambda key: key.startswith("mercury-"),
}


def load_config() -> dict:
    if CONFIG_FILE.exists():
        import json
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}


def save_config(config: dict) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    import json
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)


def get_api_key(provider: str = "openai") -> Optional[str]:
    config = load_config()
    key = config.get(f"{provider}_api_key")
    if key:
        return key
    return os.environ.get(f"{provider.upper()}_API_KEY")


def detect_provider() -> str:
    for provider in ["openai", "anthropic", "gemini", "groq", "mercury"]:
        key = get_api_key(provider)
        if key and PROVIDER_KEY_PATTERNS.get(provider, lambda k: bool(k))(key):
            return provider
    return "openai"


def set_api_key(provider: str, key: str) -> None:
    config = load_config()
    config[f"{provider}_api_key"] = key
    save_config(config)


def get_model() -> str:
    config = load_config()
    return config.get("model", "gpt-4")


def set_model(model: str) -> None:
    config = load_config()
    config["model"] = model
    save_config(config)


def get_provider() -> str:
    config = load_config()
    provider = config.get("provider", "openai")
    if provider not in SUPPORTED_PROVIDERS:
        return detect_provider()
    return provider


def list_providers() -> list:
    return SUPPORTED_PROVIDERS
