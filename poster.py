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

    # FONT LEBIH KECIL
    fontquote = loadfont(48)
    fontref = loadfont(28)

    # WRAP TEXT
    lines = textwrap.wrap(quote, width=32)

    # BATASI MAX 2 BARIS
    if len(lines) > 2:
        lines = lines[:2]

    lineheight = 70
    totalheight = len(lines) * lineheight

    y = H//2 - totalheight//2

    # WARNA KHaki LEMBUT
    textcolor = (195, 176, 145)
    shadow = (0, 0, 0)

    for line in lines:

        # shadow halus
        draw.text(
            (W//2+2, y+2),
            line,
            font=fontquote,
            fill=shadow,
            anchor="mm"
        )

        # main text
        draw.text(
            (W//2, y),
            line,
            font=fontquote,
            fill=textcolor,
            anchor="mm"
        )

        y += lineheight

    # SOURCE / AYAT DI BAWAH
    draw.text(
        (W//2, y + 60),
        ref,
        font=fontref,
        fill=(170,150,120),
        anchor="mm"
    )

    path = f"poster/{index}.png"

    img.save(
        path,
        "PNG",
        optimize=True
    )

    return path
