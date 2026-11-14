from pathlib import Path
from PIL import Image, ImageDraw

from profile_assets.config import CANVAS, FRAMES, PALETTE
from profile_assets.drawing import center_text, font, glow_dot, orbit_points, scanlines
from profile_assets.export import save_gif


def build(output: Path):
    frames = []
    for index in range(FRAMES):
        image = Image.new("RGBA", CANVAS, (*PALETTE["background"], 255))
        draw = ImageDraw.Draw(image)
        for y in range(0, CANVAS[1], 6):
            draw.line((0, y, CANVAS[0], y), fill=(18, 24, 34, 255))
        for x in range(-CANVAS[1], CANVAS[0], 38):
            draw.line((x, 0, x + CANVAS[1], CANVAS[1]), fill=(30, 21, 54, 100), width=1)
        for point in orbit_points((1010, 178), 115, 10, index * 0.18):
            glow_dot(image, point, 2, PALETTE["cyan"])
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle((62, 54, 1138, 306), radius=20, outline=(*PALETTE["purple"], 180), width=2)
        draw.rounded_rectangle((76, 68, 1124, 292), radius=14, outline=(*PALETTE["cyan"], 70), width=1)
        center_text(draw, 92, "ZAIN ALI", font(62, mono=True), PALETTE["white"], CANVAS[0])
        center_text(draw, 171, "CREATIVE DEVELOPER  /  WEBGL ARTIST", font(22, mono=True), PALETTE["cyan"], CANVAS[0])
        center_text(draw, 222, "DESIGN  •  MOTION  •  TECHNOLOGY", font(18, mono=True), PALETTE["pink"], CANVAS[0])
        scanlines(image)
        frames.append(image)
    save_gif(frames, output, duration=110)


if __name__ == "__main__":
    build(Path("assets/header.gif"))
