"""Tests for UI components."""

import pytest
from io import StringIO
import sys

from ai_cli.ui.display import format_response, print_info, print_success, print_error
from ai_cli.ui.themes import get_theme, list_themes, THEME_DEFAULT


class TestDisplay:
    def test_format_response_simple(self):
        result = format_response("Hello world")
        assert "Hello world" in result

    def test_format_response_wrapping(self):
        long_text = "word " * 100
        result = format_response(long_text, max_width=20)
        for line in result.split("\n"):
            assert len(line) <= 20

    def test_print_info(self):
        captured = StringIO()
        sys.stdout = captured
        print_info("test", "value")
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        assert "test" in output
        assert "value" in output

    def test_print_success(self):
        captured = StringIO()
        sys.stdout = captured
        print_success("test")
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        assert "test" in output

    def test_print_error(self):
        captured = StringIO()
        sys.stdout = captured
        print_error("test")
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        assert "test" in output

    def test_print_warning(self):
        captured = StringIO()
        sys.stdout = captured
        print_warning("test")
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        assert "test" in output


class TestThemes:
    def test_get_default_theme(self):
        theme = get_theme("default")
        assert theme.name == "default"

    def test_get_unknown_theme_returns_default(self):
        theme = get_theme("nonexistent")
        assert theme.name == "default"

    def test_list_themes(self):
        themes = list_themes()
        assert "default" in themes
        assert len(themes) > 0

    def test_theme_has_colors(self):
        theme = THEME_DEFAULT
        assert "header" in theme.colors
        assert "success" in theme.colors
