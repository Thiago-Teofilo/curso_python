# Reference:
# https://pillow.readthedocs.io/en/stable/reference/

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT_PATH = Path(__file__).parent
ORIGINAL_IMG = ROOT_PATH / 'original.jfif'
NEW_IMG = ROOT_PATH / 'imagem.jpeg'

size = 128, 128

with Image.open(ORIGINAL_IMG).convert("RGBA") as base:
    base = base.resize(size)

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    # get a font
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text((10, 10), "Hello", fill=(255, 255, 255, 128))
    # draw text, full opacity
    d.text((10, 60), "World", fill=(255, 255, 255, 255))

    out = Image.alpha_composite(base, txt)

    out.show()

