"""Tests for AI providers."""

import pytest
from unittest.mock import MagicMock, patch, mock_open

from ai_cli.providers.base import BaseProvider
from ai_cli.providers.openai import OpenAIProvider
from ai_cli.providers.local import LocalProvider
from ai_cli.providers.anthropic import AnthropicProvider


@pytest.fixture
def clean_env(monkeypatch, clean_config):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("CORTEX_BASE_URL", raising=False)


class TestBaseProvider:
    def test_abstract_methods(self):
        with pytest.raises(TypeError):
            BaseProvider()

    def test_repr(self):
        provider = OpenAIProvider(model="gpt-4")
        assert "OpenAIProvider" in repr(provider)
        assert "gpt-4" in repr(provider)


class TestOpenAIProvider:
    def test_init(self):
        provider = OpenAIProvider(model="gpt-4")
        assert provider.model == "gpt-4"
        assert provider.base_url == "https://api.openai.com/v1"

    def test_list_models(self):
        provider = OpenAIProvider()
        models = provider.list_models()
        assert "gpt-4" in models
        assert "gpt-4o" in models

    def test_is_available_without_key(self, clean_env):
        provider = OpenAIProvider()
        assert provider.is_available() == False

    def test_generate_without_key_raises(self, clean_env):
        provider = OpenAIProvider()
        with pytest.raises(ValueError, match="API key"):
            provider.generate("hello")

    def test_generate_with_mock(self, clean_env):
        provider = OpenAIProvider(api_key="test-key")
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "Hello there"}}],
        }
        mock_response.raise_for_status = MagicMock()
        with patch("ai_cli.providers.openai.requests.post", return_value=mock_response):
            result = provider.generate("hi")
        assert result == "Hello there"


class TestLocalProvider:
    def test_init(self):
        provider = LocalProvider(model="llama3")
        assert provider.model == "llama3"
        assert "localhost" in provider.endpoint

    def test_list_models_default(self):
        provider = LocalProvider()
        models = provider.list_models()
        assert len(models) > 0

    def test_is_available_without_server(self, clean_env):
        provider = LocalProvider(endpoint="http://localhost:99999")
        assert provider.is_available() == False

    def test_generate_with_mock(self, clean_env):
        provider = LocalProvider(endpoint="http://test:11434")
        mock_response = MagicMock()
        mock_response.json.return_value = {"response": "Neural output"}
        mock_response.raise_for_status = MagicMock()
        with patch("ai_cli.providers.local.requests.post", return_value=mock_response):
            result = provider.generate("test")
        assert result == "Neural output"


class TestAnthropicProvider:
    def test_init(self):
        provider = AnthropicProvider(model="claude-3")
        assert provider.model == "claude-3"

    def test_list_models(self):
        provider = AnthropicProvider()
        models = provider.list_models()
        assert "claude-3-opus" in models[0]

    def test_is_available_without_key(self, clean_env):
        provider = AnthropicProvider()
        assert provider.is_available() == False

    def test_generate_with_mock(self, clean_env):
        provider = AnthropicProvider(api_key="test-key")
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "content": [{"text": "Claude says hi"}],
        }
        mock_response.raise_for_status = MagicMock()
        with patch("ai_cli.providers.anthropic.requests.post", return_value=mock_response):
            result = provider.generate("hello")
        assert result == "Claude says hi"
