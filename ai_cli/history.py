"""History storage for Cortex CLI."""

import json
from datetime import datetime
from pathlib import Path

HISTORY_DIR = Path.home() / ".config" / "cortex"
HISTORY_FILE = HISTORY_DIR / "history.json"


def add_to_history(user_message: str, ai_response: str) -> None:
    entry = {
        "time": datetime.now().isoformat(),
        "user": user_message,
        "ai": ai_response,
    }
    history = _load_history()
    history.append(entry)
    _save_history(history)


def get_history(limit: int = 50) -> list:
    history = _load_history()
    return history[-limit:] if len(history) > limit else history


def clear_history() -> None:
    _save_history([])


def _load_history() -> list:
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def _save_history(history: list) -> None:
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)
