from PIL import Image
from pathlib import Path

ROOT_PATH = Path(__file__).parent
ORIGINAL_IMG = ROOT_PATH / 'original.jfif'
NEW_IMG = ROOT_PATH / 'imagem.jpeg'

pil_image = Image.open(ORIGINAL_IMG)

width, height = pil_image.size
exif = pil_image.getexif()

new_width = 640
new_height = round(height * new_width / width)

new_size = (new_width, new_height)
new_image = pil_image.resize(size=new_size)
new_image.save(
    NEW_IMG,
    optimize=True,
    quality=70,
    exif=exif
)