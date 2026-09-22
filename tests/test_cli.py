"""Tests for CLI commands."""

import pytest
from unittest.mock import patch, MagicMock

from ai_cli.commands.chat import chat_command
from ai_cli.commands.models import models_command
from ai_cli.commands.status import status_command
from ai_cli.commands.history import history_command


class TestChatCommand:
    def test_chat_with_message(self):
        args = MagicMock()
        args.model = "gpt-4"
        args.message = "Hello"
        with patch("ai_cli.commands.chat._get_provider") as mock_provider:
            mock_provider.return_value.is_available.return_value = True
            mock_provider.return_value.generate.return_value = "Response"
            chat_command(args)

    def test_chat_provider_not_available(self):
        args = MagicMock()
        args.model = "gpt-4"
        args.message = "Hello"
        with patch("ai_cli.commands.chat._get_provider") as mock_provider:
            mock_provider.return_value.is_available.return_value = False
            with pytest.raises(SystemExit):
                chat_command(args)

    def test_chat_interactive_mode(self):
        args = MagicMock()
        args.model = None
        args.message = None
        with patch("builtins.input", side_effect=["exit"]):
            with patch("ai_cli.commands.chat._get_provider") as mock_provider:
                mock_provider.return_value.is_available.return_value = True
                mock_provider.return_value.generate.return_value = "Response"
                chat_command(args)


class TestModelsCommand:
    def test_models_list(self):
        args = MagicMock()
        with patch("ai_cli.commands.models.OpenAIProvider") as mock_openai:
            mock_instance = MagicMock()
            mock_instance.is_available.return_value = True
            mock_instance.list_models.return_value = ["gpt-4", "gpt-4o"]
            mock_openai.return_value = mock_instance
            models_command(args)


class TestStatusCommand:
    def test_status(self):
        args = MagicMock()
        with patch("ai_cli.commands.status.get_provider", return_value="openai"):
            with patch("ai_cli.commands.status.get_model", return_value="gpt-4"):
                status_command(args)


class TestHistoryCommand:
    def test_history_empty(self):
        args = MagicMock()
        args.limit = 10
        with patch("ai_cli.commands.history._load_history", return_value=[]):
            history_command(args)

    def test_history_with_entries(self):
        args = MagicMock()
        args.limit = 5
        with patch("ai_cli.commands.history._load_history", return_value=[
            {"time": "2026-01-01", "user": "hi", "ai": "hello"},
        ]):
            history_command(args)
