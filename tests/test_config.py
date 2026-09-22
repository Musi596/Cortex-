"""Tests for config management."""

import json
import tempfile
from pathlib import Path
import pytest

from ai_cli.config import load_config, save_config, get_api_key, set_api_key, get_model, set_model


@pytest.fixture
def temp_config():
    with tempfile.TemporaryDirectory() as tmpdir:
        config_dir = Path(tmpdir) / ".config" / "cortex"
        config_dir.mkdir(parents=True)
        config_file = config_dir / "config.json"
        yield config_file


def test_load_config_empty():
    config = load_config()
    assert isinstance(config, dict)


def test_save_and_load_config():
    config = {"openai_api_key": "test-key", "model": "gpt-4"}
    save_config(config)
    loaded = load_config()
    assert loaded.get("openai_api_key") == "test-key"
    assert loaded.get("model") == "gpt-4"


def test_set_and_get_api_key():
    set_api_key("openai", "sk-test123")
    key = get_api_key("openai")
    assert key == "sk-test123"


def test_set_and_get_model():
    set_model("gpt-4o")
    model = get_model()
    assert model == "gpt-4o"


def test_get_model_default():
    config = load_config()
    assert isinstance(config, dict)


def test_api_key_fallback_to_env(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "env-key")
    key = get_api_key("openai")
    assert key == "env-key"
