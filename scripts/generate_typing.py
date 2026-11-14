from pathlib import Path
from PIL import Image, ImageDraw

from profile_assets.config import FRAMES, PALETTE
from profile_assets.drawing import center_text, font
from profile_assets.export import save_gif

LINES = (
    "Building Immersive 3D Web Experiences",
    "Architecting Scalable Frontend Systems",
    "Turning Ideas Into Interactive Art",
)


def build(output: Path):
    frames = []
    for index in range(FRAMES):
        image = Image.new("RGBA", (900, 76), (*PALETTE["background"], 255))
        draw = ImageDraw.Draw(image)
        line = LINES[index % len(LINES)]
        visible = line[: 8 + ((index * 5) % (len(line) - 7))]
        center_text(draw, 16, f"> {visible}_", font(21, mono=True), PALETTE["cyan"], 900)
        frames.append(image)
    save_gif(frames, output, duration=150)


if __name__ == "__main__":
    build(Path("assets/typing.gif"))
