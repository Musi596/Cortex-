"""Cortex - AI CLI terminal manager."""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Cortex AI CLI")
    parser.add_argument("--version", action="version", version="cortex 0.1.0")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("chat", help="Chat with AI")
    subparsers.add_parser("models", help="List models")
    subparsers.add_parser("status", help="Show status")
    subparsers.add_parser("history", help="Show history")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)
    print(f"Running: {args.command}")


if __name__ == "__main__":
    main()
