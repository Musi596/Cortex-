"""Status command for Cortex CLI."""

import platform
import sys
from datetime import datetime

from ai_cli.ui.display import print_header, print_info, print_success
from ai_cli.config import get_provider, get_model
from ai_cli.providers.openai import OpenAIProvider
from ai_cli.providers.local import LocalProvider
from ai_cli.providers.anthropic import AnthropicProvider
from ai_cli.providers.gemini import GeminiProvider
from ai_cli.providers.groq import GroqProvider
from ai_cli.providers.mercury import MercuryProvider


def status_command(args):
    print_header("Cortex CLI Status")

    print_info("Version", "0.1.0")
    print_info("Python", sys.version.split()[0])
    print_info("Platform", platform.system())
    print_info("Provider", get_provider())
    print_info("Model", get_model())
    print_info("Timestamp", datetime.now().isoformat())

    providers = [
        ("OpenAI", OpenAIProvider()),
        ("Local", LocalProvider()),
        ("Anthropic", AnthropicProvider()),
        ("Gemini", GeminiProvider()),
        ("Groq", GroqProvider()),
        ("Mercury", MercuryProvider()),
    ]

    print()
    for name, provider in providers:
        if provider.is_available():
            print_success(f"{name}: connected")
        else:
            print_info(name, "not connected")

    print()
