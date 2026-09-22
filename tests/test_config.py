"""Tests for config management."""

import pytest

from ai_cli.config import load_config, save_config, get_api_key, set_api_key, get_model, set_model


def test_load_config_empty():
    config = load_config()
    assert isinstance(config, dict)


def test_save_and_load_config():
    config = {"openai_api_key": "test-key", "model": "gpt-4"}
    save_config(config)
    loaded = load_config()
    assert loaded.get("openai_api_key") == "test-key"
    assert loaded.get("model") == "gpt-4"


def test_set_and_get_api_key(clean_config):
    set_api_key("openai", "sk-test123")
    key = get_api_key("openai")
    assert key == "sk-test123"


def test_set_and_get_model(clean_config):
    set_model("gpt-4o")
    model = get_model()
    assert model == "gpt-4o"


def test_get_model_default():
    config = load_config()
    assert isinstance(config, dict)


def test_api_key_fallback_to_env(clean_env, monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "env-key")
    key = get_api_key("openai")
    assert key == "env-key"
