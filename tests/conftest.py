"""Shared test fixtures for Cortex CLI."""

import pytest
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
