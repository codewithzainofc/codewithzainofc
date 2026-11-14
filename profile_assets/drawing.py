"""Small, dependency-light drawing primitives shared by asset scripts."""

import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from .config import PALETTE

ROOT_FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
MONO_FONT = "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"


def font(size: int, mono: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(MONO_FONT if mono else ROOT_FONT, size)


def gradient(size, left, right, phase=0):
    image = Image.new("RGB", size)
    pixels = image.load()
    width, height = size
    for x in range(width):
        t = ((x / max(1, width - 1)) + phase) % 1.0
        color = tuple(int(left[i] * (1 - t) + right[i] * t) for i in range(3))
        for y in range(height):
            pixels[x, y] = color
    return image


def glow_dot(base, xy, radius, color, strength=3):
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    for step in range(strength, 0, -1):
        alpha = int(80 / step)
        r = radius * step
        draw.ellipse((xy[0] - r, xy[1] - r, xy[0] + r, xy[1] + r), fill=(*color, alpha))
    layer = layer.filter(ImageFilter.GaussianBlur(radius * 1.5))
    base.alpha_composite(layer)
    ImageDraw.Draw(base).ellipse(
        (xy[0] - radius, xy[1] - radius, xy[0] + radius, xy[1] + radius),
        fill=(*color, 230),
    )


def center_text(draw, y, text, font_obj, fill, width):
    box = draw.textbbox((0, 0), text, font=font_obj)
    draw.text(((width - (box[2] - box[0])) // 2, y), text, font=font_obj, fill=fill)


def scanlines(image, spacing=4):
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for y in range(0, image.height, spacing):
        draw.line((0, y, image.width, y), fill=(255, 255, 255, 10))
    image.alpha_composite(overlay)


def orbit_points(center, radius, count, phase):
    return [
        (
            int(center[0] + math.cos(phase + 2 * math.pi * i / count) * radius),
            int(center[1] + math.sin(phase + 2 * math.pi * i / count) * radius),
        )
        for i in range(count)
    ]
