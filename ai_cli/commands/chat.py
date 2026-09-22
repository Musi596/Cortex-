"""Chat command for Cortex CLI."""

import sys

from ai_cli.ui.display import print_banner, print_header, print_info, format_response
from ai_cli.config import get_model, get_provider
from ai_cli.utils import sanitize_input
from ai_cli.providers.openai import OpenAIProvider
from ai_cli.providers.local import LocalProvider
from ai_cli.providers.anthropic import AnthropicProvider


def chat_command(args):
    print_banner()
    model = args.model or get_model()
    provider_name = get_provider()

    provider = _get_provider(provider_name, model)
    if not provider.is_available():
        print("Provider not available. Configure API key first.")
        sys.exit(1)

    print_header(f"Chat — {provider}")

    if args.message:
        message = sanitize_input(args.message)
        response = provider.generate(message)
        print(f"\n\033[1mYou:\033[0m {message}")
        print(f"\033[1mAI:\033[0m\n{format_response(response)}")
    else:
        print("Interactive mode. Type 'exit' to quit.\n")
        while True:
            try:
                user_input = input("\033[1mYou:\033[0m ")
                if user_input.lower() in ("exit", "quit", "q"):
                    break
                message = sanitize_input(user_input)
                response = provider.generate(message)
                print(f"\033[1mAI:\033[0m\n{format_response(response)}")
            except (KeyboardInterrupt, EOFError):
                print("\nGoodbye!")
                break


def _get_provider(name: str, model: str):
    if name == "local":
        return LocalProvider(model=model)
    if name == "anthropic":
        return AnthropicProvider(model=model)
    return OpenAIProvider(model=model)
