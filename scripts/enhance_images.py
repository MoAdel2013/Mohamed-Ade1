from PIL import Image, ImageFilter
from pathlib import Path

FILES = [
    "first_picture_alone.png",
    "eighth_picture (4).png",
    "fifth_picture_alone.png",
    "fourth_picture.png",
    "second_picture_alone.png",
    "ninth_picture.png",
    "third_picture_alone.png",
    "seventh_picture.png",
    "eleventh_picture.png",
    "sixth_picture_alone.png",
]

out = Path("enhanced")
out.mkdir(exist_ok=True)

for name in FILES:
    src = Path(name)
    if not src.exists():
        raise FileNotFoundError(src)
    im = Image.open(src).convert("RGB")
    # 3x enlargement with high-quality Lanczos resampling, followed by
    # restrained sharpening to recover edge definition without changing
    # the original composition or colors.
    w, h = im.size
    im = im.resize((w * 3, h * 3), Image.Resampling.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=115, threshold=3))
    im.save(out / (src.stem + ".jpg"), "JPEG", quality=95, optimize=True, progressive=True)
