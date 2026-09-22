# Providers

Cortex supports multiple AI providers:

## OpenAI
Uses the OpenAI Chat Completions API. Set `OPENAI_API_KEY` to enable.

## Anthropic
Uses the Anthropic Messages API. Set `ANTHROPIC_API_KEY` to enable.

## Local Models
Uses Ollama-compatible API. Set `CORTEX_BASE_URL` (default: `http://localhost:11434`).

Supported local models:
- Llama 3
- Mistral
- Phi-3
