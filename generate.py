"""Generate every local animated profile asset."""

from pathlib import Path

from scripts.generate_footer import build as build_footer
from scripts.generate_header import build as build_header
from scripts.generate_typing import build as build_typing


def main():
    output = Path("assets")
    build_header(output / "header.gif")
    build_typing(output / "typing.gif")
    build_footer(output / "footer.gif")
    print("Generated assets/header.gif, assets/typing.gif, assets/footer.gif")


if __name__ == "__main__":
    main()
