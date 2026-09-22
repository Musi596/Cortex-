"""History command for Cortex CLI."""

import json
from pathlib import Path
from datetime import datetime

from ai_cli.ui.display import print_header, print_info, print_warning
from ai_cli.config import load_config


HISTORY_FILE = Path.home() / ".config" / "cortex" / "history.json"


def history_command(args):
    limit = getattr(args, "limit", 10)
    print_header("Chat History")

    history = _load_history()
    entries = history[-limit:] if len(history) > limit else history

    if not entries:
        print_warning("No history yet")
        return

    for i, entry in enumerate(entries, 1):
        timestamp = entry.get("time", "unknown")
        user_msg = entry.get("user", "")[:80]
        ai_msg = entry.get("ai", "")[:80]
        print(f"\n  \033[90m[{i}] {timestamp}\033[0m")
        print(f"  \033[1mYou:\033[0m {user_msg}")
        print(f"  \033[1mAI:\033[0m {ai_msg}")


def _load_history() -> list:
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []
