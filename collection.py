import os
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont
import numpy as np

W, H = 1080, 1080

quotes = [
"Sesungguhnya bersama kesulitan ada kemudahan. (QS Al-Insyirah:6)",
"Barang siapa bertakwa kepada Allah niscaya Dia akan memberinya jalan keluar. (QS At-Talaq:2)",
"Sebaik-baik manusia adalah yang paling bermanfaat bagi manusia lain. (HR Ahmad)",
"Allah tidak membebani seseorang melainkan sesuai kesanggupannya. (QS Al-Baqarah:286)",
"Sesungguhnya Allah bersama orang-orang yang sabar. (QS Al-Baqarah:153)",
"Barang siapa memudahkan kesulitan orang lain, Allah akan memudahkannya di dunia dan akhirat. (HR Muslim)",
"Jangan bersedih, sesungguhnya Allah bersama kita. (QS At-Taubah:40)",
"Dan bertawakallah kepada Allah, cukuplah Allah sebagai pelindung. (QS Al-Ahzab:3)"
]

def make_background():
    base = np.zeros((H, W, 3), dtype=np.uint8)

    c1 = np.array([random.randint(10,80), random.randint(10,80), random.randint(80,200)])
    c2 = np.array([random.randint(80,200), random.randint(10,80), random.randint(10,80)])

    for y in range(H):
        t = y / H
        color = (1-t)*c1 + t*c2
        base[y,:,:] = color

    noise = np.random.randint(0,25,(H,W,3))
    base = np.clip(base + noise,0,255)

    return Image.fromarray(base.astype("uint8"))

def load_font(size):
    paths = [
        "fonts/PlayfairDisplay-Bold.ttf",
        "fonts/LibreBaskerville-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
    ]

    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)

    return ImageFont.load_default()

def run():

    os.makedirs("outputs", exist_ok=True)

    bg = make_background()
    draw = ImageDraw.Draw(bg)

    quote = random.choice(quotes)

    if len(quote) > 120:
        quote = quote[:120] + "..."

    # FONT dikurangi sekitar 10%
    font = load_font(54)

    lines = textwrap.wrap(quote, width=24)

    line_height = 65
    y = H//2 - (len(lines)*line_height)//2

    for line in lines:

        draw.text(
            (W//2, y),
            line,
            font=font,
            fill=(255,255,255),
            anchor="mm"
        )

        y += line_height

    fname = f"outputs/viral_{random.randint(1000,9999)}.png"
    bg.save(fname)

    print("generated:", fname)

if __name__ == "__main__":
    run()
