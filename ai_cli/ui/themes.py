"""Color themes for Cortex CLI terminal output."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Theme:
    name: str
    colors: Dict[str, str]


THEME_DEFAULT = Theme(
    name="default",
    colors={
        "header": "cyan",
        "success": "green",
        "error": "red",
        "warning": "yellow",
        "info": "white",
        "accent": "bright_cyan",
        "dim": "bright_black",
    },
)

THEME_DARK = Theme(
    name="dark",
    colors={
        "header": "bright_cyan",
        "success": "bright_green",
        "error": "bright_red",
        "warning": "bright_yellow",
        "info": "white",
        "accent": "cyan",
        "dim": "bright_black",
    },
)

THEME_NATURE = Theme(
    name="nature",
    colors={
        "header": "green",
        "success": "bright_green",
        "error": "red",
        "warning": "yellow",
        "info": "bright_white",
        "accent": "bright_green",
        "dim": "black",
    },
)

AVAILABLE_THEMES = {
    "default": THEME_DEFAULT,
    "dark": THEME_DARK,
    "nature": THEME_NATURE,
}


def get_theme(name: str = "default") -> Theme:
    return AVAILABLE_THEMES.get(name, THEME_DEFAULT)


def list_themes() -> list:
    return list(AVAILABLE_THEMES.keys())
