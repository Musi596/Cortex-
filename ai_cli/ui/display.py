"""Terminal display utilities for Cortex CLI."""

from typing import Optional


def print_header(title: str, width: int = 60) -> None:
    line = "=" * width
    print(f"\n{line}")
    print(f"  {title}")
    print(f"{line}\n")


def print_info(label: str, value: str, spacer: str = ": ") -> None:
    print(f"  \033[1m{label}\033[0m{spacer}{value}")


def print_success(message: str) -> None:
    print(f"  \033[92m\u2713 {message}\033[0m")


def print_error(message: str) -> None:
    print(f"  \033[91m\u2717 {message}\033[0m")


def print_warning(message: str) -> None:
    print(f"  \033[93m\u26a0 {message}\033[0m")


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
    print("\033[1;36m")
    print("╔══════════════════════════════════════╗")
    print("║         C O R T E X  CLI            ║")
    print("║    AI Management in Your Terminal    ║")
    print("╚══════════════════════════════════════╝")
    print("\033[0m")
