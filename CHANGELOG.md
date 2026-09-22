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
- Full test suite (38 tests passing)
- Input sanitization in chat command
- Provider class exports via __init__
- README with badges, features table, provider matrix

### Bug Fixes
- Fix: add top-level requests import in local provider
- Fix: add top-level requests import in anthropic provider
- Fix: restore cli.py with correct Python code after accidental overwrite

### Test Fixes
- Add clean_config and clean_env fixtures for test isolation
- Fix config tests to use proper fixtures
- Fix provider tests for proper environment cleanup
- Fix missing print_warning import in UI tests

### Performance
- Pre-import requests in providers instead of lazy import
