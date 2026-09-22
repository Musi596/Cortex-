# API Reference

## Module: ai_cli.cli

Main CLI entry point.

- `main()` — Parse arguments and dispatch commands

## Module: ai_cli.config

Configuration management.

- `load_config()` → `dict`
- `save_config(config)` → `None`
- `get_api_key(provider)` → `str | None`
- `set_api_key(provider, key)` → `None`
- `get_model()` → `str`
- `set_model(model)` → `None`
- `get_provider()` → `str`
- `list_providers()` → `list`

## Module: ai_cli.providers.base

Abstract base provider.

- `BaseProvider.generate(prompt)` → `str`
- `BaseProvider.list_models()` → `list`
- `BaseProvider.is_available()` → `bool`

## Module: ai_cli.providers.openai

OpenAI implementation.

- `OpenAIProvider(model, api_key)`

## Module: ai_cli.providers.anthropic

Anthropic implementation.

- `AnthropicProvider(model, api_key)`

## Module: ai_cli.providers.gemini

Google Gemini implementation.

- `GeminiProvider(model, api_key)`
- Base URL: `https://generativelanguage.googleapis.com/v1beta`

## Module: ai_cli.providers.groq

Groq implementation (ultra-fast inference).

- `GroqProvider(model, api_key)`
- Base URL: `https://api.groq.com/openai/v1`

## Module: ai_cli.providers.mercury

Mercury implementation.

- `MercuryProvider(model, api_key)`
- Base URL: `https://api.mercury.ai/v1`

## Module: ai_cli.providers.local

Local model implementation.

- `LocalProvider(model, endpoint)`

## Module: ai_cli.ui.display

Terminal display utilities.

- `print_header(title)`
- `print_info(label, value)`
- `print_success(message)`
- `print_error(message)`
- `print_warning(message)`
- `format_response(text, max_width)`
- `print_banner()`

## Module: ai_cli.ui.themes

Color themes.

- `get_theme(name)` → `Theme`
- `list_themes()` → `list`

## Module: ai_cli.ui.progress

Progress indicators.

- `Spinner(message)` — Terminal spinner
- `show_progress(steps, func)` — Step-by-step progress

## Module: ai_cli.utils

Utility functions.

- `sanitize_input(text)` → `str`
- `format_duration(seconds)` → `str`
- `truncate(text, length)` → `str`
- `validate_api_key(provider, key)` → `bool`
- `parse_model_alias(model)` → `str`
- `escape_markdown(text)` → `str`
