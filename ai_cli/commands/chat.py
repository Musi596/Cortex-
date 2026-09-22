"""Chat command for Cortex CLI."""

import sys

from ai_cli.ui.display import print_banner, print_header, print_info, print_error, format_response
from ai_cli.config import get_model, get_provider
from ai_cli.utils import sanitize_input, parse_model_alias
from ai_cli.providers.openai import OpenAIProvider
from ai_cli.providers.local import LocalProvider
from ai_cli.providers.anthropic import AnthropicProvider
from ai_cli.providers.gemini import GeminiProvider
from ai_cli.providers.groq import GroqProvider
from ai_cli.providers.mercury import MercuryProvider


def chat_command(args):
    print_banner()
    model = parse_model_alias(args.model or get_model())
    provider_name = get_provider()

    provider = _get_provider(provider_name, model)
    if not provider.is_available():
        print("Provider not available. Configure API key first.")
        sys.exit(1)

    print_header(f"Chat — {provider}")

    if args.message:
        message = sanitize_input(args.message)
        response = _safe_generate(provider, message)
        if response:
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
                response = _safe_generate(provider, message)
                if response:
                    print(f"\033[1mAI:\033[0m\n{format_response(response)}")
            except (KeyboardInterrupt, EOFError):
                print("\nGoodbye!")
                break


def _safe_generate(provider, message):
    try:
        return provider.generate(message)
    except Exception as e:
        print_error(f"Error: {e}")
        return None


def _get_provider(name: str, model: str):
    if name == "local":
        return LocalProvider(model=model)
    if name == "anthropic":
        return AnthropicProvider(model=model)
    if name == "gemini":
        return GeminiProvider(model=model)
    if name == "groq":
        return GroqProvider(model=model)
    if name == "mercury":
        return MercuryProvider(model=model)
    return OpenAIProvider(model=model)
