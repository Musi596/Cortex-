# Commands Reference

## cortex chat

Start a chat session with AI.

**Options:**
- `--model` — Model to use
- `--message, -m` — Single message to send

**Examples:**
```bash
cortex chat --message "Hello"
cortex chat --model gpt-4 --message "Explain Python"
cortex chat  # Interactive mode
```

## cortex models

List available models for each provider.

**Examples:**
```bash
cortex models
```

## cortex status

Show current status including version, provider, and model.

**Examples:**
```bash
cortex status
```

## cortex history

Show chat history.

**Options:**
- `--limit, -l` — Number of entries (default: 10)

**Examples:**
```bash
cortex history
cortex history --limit 50
```
