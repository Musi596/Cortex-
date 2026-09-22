"""Shared test fixtures for Cortex CLI."""

import pytest
import tempfile
from pathlib import Path
from unittest.mock import MagicMock


@pytest.fixture
def mock_args():
    return MagicMock()


@pytest.fixture
def mock_provider():
    provider = MagicMock()
    provider.is_available.return_value = True
    provider.generate.return_value = "Mock response"
    provider.list_models.return_value = ["model-1", "model-2"]
    return provider


@pytest.fixture
def sample_history():
    return [
        {"time": "2026-01-01T10:00:00", "user": "Hello", "ai": "Hi there"},
        {"time": "2026-01-01T11:00:00", "user": "How are you?", "ai": "I'm fine!"},
    ]


@pytest.fixture
def clean_config(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        config_dir = Path(tmpdir) / ".config" / "cortex"
        config_dir.mkdir(parents=True)
        monkeypatch.setattr("ai_cli.config.CONFIG_DIR", config_dir)
        monkeypatch.setattr("ai_cli.config.CONFIG_FILE", config_dir / "config.json")
        yield config_dir / "config.json"


@pytest.fixture
def clean_env(monkeypatch, clean_config):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("GROQ_API_KEY", raising=False)
    monkeypatch.delenv("MERCURY_API_KEY", raising=False)
    monkeypatch.delenv("CORTEX_BASE_URL", raising=False)
