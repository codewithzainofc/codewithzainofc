"""Validate generated assets, README links, and size budgets."""

from pathlib import Path
import re

from profile_assets.config import ASSETS
from profile_assets.export import inspect_gif


def main():
    root = Path(__file__).parent
    readme = (root / "README.md").read_text()
    errors = []
    for spec in ASSETS:
        path = root / "assets" / spec.name
        if not path.exists():
            errors.append(f"missing {path}")
            continue
        size, frames, bytes_used = inspect_gif(path)
        if size != spec.size:
            errors.append(f"{spec.name}: expected {spec.size}, got {size}")
        if frames != spec.frames:
            errors.append(f"{spec.name}: expected {spec.frames} frames, got {frames}")
        if bytes_used > spec.budget_kb * 1024:
            errors.append(f"{spec.name}: {bytes_used // 1024} KiB exceeds {spec.budget_kb} KiB")
        if f"assets/{spec.name}" not in readme:
            errors.append(f"README does not reference assets/{spec.name}")
    if "usernamezain" not in readme or "zaindev.me" not in readme:
        errors.append("README lost supplied profile facts")
    if errors:
        raise SystemExit("\n".join(errors))
    print("Validated dimensions, frame counts, budgets, and README references.")


if __name__ == "__main__":
    main()
