# Setup

## Installation

```bash
pip install -e .
```

## Configuration

Create a config file at `~/.config/cortex/config.json`:

```json
{
    "openai_api_key": "sk-...",
    "anthropic_api_key": "sk-ant-...",
    "provider": "openai",
    "model": "gpt-4"
}
```

Or set environment variables:

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export CORTEX_PROVIDER="openai"
export CORTEX_MODEL="gpt-4"
```
