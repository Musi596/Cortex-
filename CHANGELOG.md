# Changelog
All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-09-22
### Features
- Initial CLI with chat, models, status, history commands
- OpenAI provider with chat completions API
- Anthropic provider with Messages API
- Local model provider (Ollama-compatible)
- Config management with env variable fallback
- Colored terminal output with themes
- Chat history storage
- Spinner and progress indicators
- Full test suite
- Input sanitization in chat command
- Provider class exports via __init__
- README with badges, features table, provider matrix

### Bug Fixes
- Move requests import to top of OpenAI provider for performance

### Performance
- Pre-import requests in OpenAI provider instead of lazy import
