"""Models command for Cortex CLI."""

from ai_cli.ui.display import print_header, print_info, print_success
from ai_cli.providers.openai import OpenAIProvider
from ai_cli.providers.local import LocalProvider
from ai_cli.providers.anthropic import AnthropicProvider


def models_command(args):
    print_header("Available Models")

    providers = [
        ("OpenAI", OpenAIProvider()),
        ("Local", LocalProvider()),
        ("Anthropic", AnthropicProvider()),
    ]

    for name, provider in providers:
        if provider.is_available():
            print_success(f"{name}:")
            models = provider.list_models()
            for m in models:
                print_info(m, "available")
        else:
            print_info(name, "not configured")
        print()
