"""Utility functions for Cortex CLI."""

import re
from typing import Optional


def sanitize_input(text: str) -> str:
    """Remove potentially harmful characters from input."""
    return text.strip()[:10000]


def format_duration(seconds: float) -> str:
    """Format seconds into human-readable duration."""
    if seconds < 1:
        return f"{seconds * 1000:.0f}ms"
    if seconds < 60:
        return f"{seconds:.2f}s"
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes}m {secs}s"


def truncate(text: str, length: int = 100) -> str:
    """Truncate text to specified length with ellipsis."""
    if len(text) <= length:
        return text
    return text[: length - 3] + "..."


def validate_api_key(provider: str, key: str) -> bool:
    """Basic API key validation."""
    if not key:
        return False
    if provider == "openai":
        return key.startswith("sk-") and len(key) > 20
    if provider == "anthropic":
        return key.startswith("sk-ant-") and len(key) > 20
    if provider == "gemini":
        return key.startswith("AIza") and len(key) > 30
    if provider == "groq":
        return key.startswith("gsk_") and len(key) > 20
    if provider == "mercury":
        return key.startswith("mercury-") and len(key) > 20
    return len(key) > 10


def parse_model_alias(model: str) -> str:
    """Convert common model aliases to full names."""
    aliases = {
        "gpt": "gpt-4",
        "gpt4": "gpt-4",
        "gpt-4": "gpt-4",
        "gpt4o": "gpt-4o",
        "gpt-4o": "gpt-4o",
        "claude": "claude-3-opus-20240229",
        "claude3": "claude-3-opus-20240229",
        "llama": "llama3",
        "llama3": "llama3",
        "mistral": "mistral",
        "phi": "phi3",
        "gemini": "gemini-2.0-flash",
        "gem": "gemini-1.5-pro",
        "gemini15": "gemini-1.5-pro",
        "gem15": "gemini-1.5-pro",
        "gemma": "gemma-7b-it",
        "llama33": "llama-3.3-70b-versatile",
        "llama-33": "llama-3.3-70b-versatile",
        "mercury": "mercury-standard",
    }
    return aliases.get(model.lower(), model)


def escape_markdown(text: str) -> str:
    """Escape markdown special characters."""
    special = r"\`*_{}[]()>#+-.!"
    return re.sub(r"([" + re.escape(special) + r"])", r"\\\1", text)
