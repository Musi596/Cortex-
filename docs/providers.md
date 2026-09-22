# Providers

Cortex supports multiple AI providers:

## OpenAI
Uses the OpenAI Chat Completions API. Set `OPENAI_API_KEY` to enable.

### Models
- gpt-4, gpt-4-turbo, gpt-3.5-turbo, gpt-4o, gpt-4o-mini

## Anthropic
Uses the Anthropic Messages API. Set `ANTHROPIC_API_KEY` to enable.

### Models
- claude-3-opus-20240229, claude-3-sonnet-20240229, claude-3-haiku-20240924

## Gemini
Uses the Google Gemini API. Set `GEMINI_API_KEY` to enable.

### Models
- gemini-1.5-pro, gemini-1.5-flash, gemini-1.5-flash-8b, gemini-2.0-flash

## Groq
Uses the Groq API (ultra-fast inference). Set `GROQ_API_KEY` to enable.

### Models
- llama-3.3-70b-versatile, llama-3.1-70b-versatile, llama-3.1-8b-instant, mixtral-8x7b-32768, gemma-7b-it

## Mercury
Uses the Mercury API. Set `MERCURY_API_KEY` to enable.

### Models
- mercury-standard, mercury-fast, mercury-vision

## Local Models
Uses Ollama-compatible API. Set `CORTEX_BASE_URL` (default: `http://localhost:11434`).

Supported local models:
- Llama 3
- Mistral
- Phi-3
