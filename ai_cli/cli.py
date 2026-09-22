import argparse
import sys

from ai_cli.commands.chat import chat_command
from ai_cli.commands.models import models_command
from ai_cli.commands.status import status_command
from ai_cli.commands.history import history_command
from ai_cli.version import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="cortex",
        description="Manage AI in your terminal — write API or connect local neural networks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Run 'cortex <command> --help' for more info.",
    )
    parser.add_argument("--version", action="version", version=f"cortex {__version__}")
    parser.add_argument("--status", action="store_true", help="Show status (shorthand)")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    chat_parser = subparsers.add_parser("chat", help="Start a chat session")
    chat_parser.add_argument("--model", default=None, help="Model to use")
    chat_parser.add_argument("--message", "-m", default=None, help="Message to send")

    models_parser = subparsers.add_parser("models", help="List available models")

    status_parser = subparsers.add_parser("status", help="Show status")

    history_parser = subparsers.add_parser("history", help="Show chat history")
    history_parser.add_argument("--limit", "-l", type=int, default=10, help="Limit entries")

    args = parser.parse_args()

    if args.status:
        status_command(args)
        sys.exit(0)

    if not args.command:
        parser.print_help()
        sys.exit(0)

    commands = {
        "chat": chat_command,
        "models": models_command,
        "status": status_command,
        "history": history_command,
    }

    handler = commands.get(args.command)
    if handler:
        handler(args)


if __name__ == "__main__":
    main()
