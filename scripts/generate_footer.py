from pathlib import Path
from PIL import Image, ImageDraw

from profile_assets.config import CANVAS, FRAMES, PALETTE
from profile_assets.drawing import glow_dot, orbit_points
from profile_assets.export import save_gif


def build(output: Path):
    frames = []
    size = (1200, 180)
    for index in range(FRAMES):
        image = Image.new("RGBA", size, (*PALETTE["background"], 255))
        draw = ImageDraw.Draw(image)
        draw.polygon([(0, 0), (size[0], 0), (size[0], 85), (0, 180)], fill=(*PALETTE["purple"], 90))
        draw.line((0, 178, size[0], 80), fill=(*PALETTE["cyan"], 220), width=3)
        draw.line((0, 180, size[0], 100), fill=(*PALETTE["pink"], 150), width=2)
        for point in orbit_points((600, 118), 480, 18, index * 0.12):
            glow_dot(image, point, 2, PALETTE["cyan"])
        frames.append(image)
    save_gif(frames, output, duration=110)


if __name__ == "__main__":
    build(Path("assets/footer.gif"))
