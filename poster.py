import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = 1200
H = 1200


def loadfont(size):

    paths = [
        "fonts/PlayfairDisplay-Bold.ttf",
        "fonts/Merriweather-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
    ]

    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)

    return ImageFont.load_default()


def render(background, quote, ref, index):

    os.makedirs("poster", exist_ok=True)

    img = background.resize((W, H))
    draw = ImageDraw.Draw(img)

    fontquote = loadfont(64)   # font utama
    fontref = loadfont(34)     # referensi ayat kecil

    # wrap quote
    lines = textwrap.wrap(quote, width=28)

    if len(lines) > 3:
        lines = lines[:3]

    lineheight = 80
    totalheight = len(lines) * lineheight

    y = H//2 - totalheight//2

    for line in lines:

        # shadow
        draw.text(
            (W//2+2, y+2),
            line,
            font=fontquote,
            fill=(0,0,0),
            anchor="mm"
        )

        # glow
        draw.text(
            (W//2, y),
            line,
            font=fontquote,
            fill=(255,255,255),
            anchor="mm"
        )

        y += lineheight

    # reference ayat / hadits
    draw.text(
        (W//2, y+30),
        ref,
        font=fontref,
        fill=(255,215,120),
        anchor="mm"
    )

    path = f"poster/{index}.png"

    img.save(
        path,
        "PNG",
        optimize=True
    )

    return path
