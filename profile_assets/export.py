"""GIF export and validation helpers."""

from pathlib import Path
from PIL import Image


def save_gif(frames, path: Path, duration=100):
    path.parent.mkdir(parents=True, exist_ok=True)
    frames[0].convert("P", palette=Image.Palette.ADAPTIVE).save(
        path,
        save_all=True,
        append_images=[frame.convert("P", palette=Image.Palette.ADAPTIVE) for frame in frames[1:]],
        duration=duration,
        loop=0,
        optimize=True,
        disposal=2,
    )


def inspect_gif(path: Path):
    with Image.open(path) as image:
        return image.size, getattr(image, "n_frames", 1), path.stat().st_size
