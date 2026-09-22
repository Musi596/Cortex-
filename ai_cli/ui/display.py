"""Terminal display utilities for Cortex CLI."""

import sys
from typing import Optional

_USE_UNICODE = True
try:
    if sys.stdout.encoding and "utf" not in sys.stdout.encoding.lower():
        _USE_UNICODE = False
except Exception:
    _USE_UNICODE = False

_SYMBOLS = {
    "success": "✓" if _USE_UNICODE else "+",
    "error": "✗" if _USE_UNICODE else "x",
    "warning": "⚠" if _USE_UNICODE else "!",
}


def _print(text: str) -> None:
    try:
        print(text)
    except UnicodeEncodeError:
        if _USE_UNICODE:
            _REPLACEMENTS = {
                "✓": "+",
                "✗": "x",
                "⚠": "!",
                "╔": "=",
                "╗": "=",
                "║": "|",
                "╚": "=",
                "═": "=",
                "─": "-",
                " ": " ",
            }
            for char, replacement in _REPLACEMENTS.items():
                text = text.replace(char, replacement)
            try:
                print(text)
            except Exception:
                pass


def print_header(title: str, width: int = 60) -> None:
    line = "=" * width
    _print("")
    _print(line)
    _print(f"  {title}")
    _print(f"{line}")
    _print("")


def print_info(label: str, value: str, spacer: str = ": ") -> None:
    _print(f"  \033[1m{label}\033[0m{spacer}{value}")


def print_success(message: str) -> None:
    _print(f"  \033[92m{_SYMBOLS['success']} {message}\033[0m")


def print_error(message: str) -> None:
    _print(f"  \033[91m{_SYMBOLS['error']} {message}\033[0m")


def print_warning(message: str) -> None:
    _print(f"  \033[93m{_SYMBOLS['warning']} {message}\033[0m")


def format_response(text: str, max_width: int = 80) -> str:
    words = text.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= max_width:
            current = current + " " + word if current else word
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return "\n".join(lines)


def print_banner() -> None:
    if _USE_UNICODE:
        try:
            _print("")
            _print("\033[1;36m")
            _print("╔══════════════════════════════════════╗")
            _print("║         C O R T E X  CLI            ║")
            _print("║    AI Management in Your Terminal    ║")
            _print("╚══════════════════════════════════════╝")
            _print("\033[0m")
            return
        except Exception:
            pass
    _print("")
    _print("=" * 42)
    _print("  C O R T E X  CLI")
    _print("  AI Management in Your Terminal")
    _print("=" * 42)
    _print("")
