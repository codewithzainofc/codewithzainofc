"""Single source of truth for the profile artwork."""

from dataclasses import dataclass

CANVAS = (1200, 360)
FRAMES = 12
PALETTE = {
    "background": (13, 17, 23),
    "cyan": (0, 209, 255),
    "purple": (112, 0, 255),
    "pink": (255, 0, 92),
    "white": (229, 231, 235),
    "muted": (139, 148, 158),
}


@dataclass(frozen=True)
class AssetSpec:
    name: str
    size: tuple[int, int]
    frames: int
    budget_kb: int


ASSETS = (
    AssetSpec("header.gif", (1200, 360), FRAMES, 900),
    AssetSpec("typing.gif", (900, 76), FRAMES, 300),
    AssetSpec("footer.gif", (1200, 180), FRAMES, 500),
)
