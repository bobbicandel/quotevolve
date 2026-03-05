import os
import random
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 1024
HEIGHT = 1024

OUTPUT = "outputs"
os.makedirs(OUTPUT, exist_ok=True)

QUOTES = [
("Allah tidak membebani seseorang melainkan sesuai dengan kesanggupannya","QS Al-Baqarah 286"),
("Sesungguhnya bersama kesulitan ada kemudahan","QS Al-Insyirah 6"),
("Barangsiapa bertakwa kepada Allah niscaya Dia akan memberikan jalan keluar","QS At-Talaq 2"),
("Sebaik-baik manusia adalah yang paling bermanfaat bagi manusia lain","HR Ahmad"),
("Dunia adalah penjara bagi orang mukmin dan surga bagi orang kafir","HR Muslim"),
("Barangsiapa menempuh jalan untuk mencari ilmu Allah akan mudahkan jalan menuju surga","HR Muslim"),
("Sesungguhnya Allah mencintai orang yang bertawakal","QS Ali Imran 159"),
]

def cinematic_background():

    base = Image.new("RGB",(WIDTH,HEIGHT))
    px = base.load()

    c1 = (
        random.randint(10,40),
        random.randint(10,40),
        random.randint(60,120)
    )

    c2 = (
        random.randint(120,180),
        random.randint(80,120),
        random.randint(20,60)
    )

    cx = WIDTH/2
    cy = HEIGHT/2
    maxdist = (cx**2 + cy**2)**0.5

    for y in range(HEIGHT):
        for x in range(WIDTH):

            dx = x-cx
            dy = y-cy
            d = (dx*dx + dy*dy)**0.5

            t = d/maxdist

            r = int(c1[0]*(1-t)+c2[0]*t)
            g = int(c1[1]*(1-t)+c2[1]*t)
            b = int(c1[2]*(1-t)+c2[2]*t)

            px[x,y]=(r,g,b)

    return base


def add_vignette(img):

    overlay = Image.new("RGBA",(WIDTH,HEIGHT),(0,0,0,0))
    d = ImageDraw.Draw(overlay)

    for i in range(400):
        alpha = int(i*0.35)
        d.rectangle(
            (i,i,WIDTH-i,HEIGHT-i),
            outline=(0,0,0,alpha)
        )

    img = Image.alpha_composite(img.convert("RGBA"),overlay)

    return img.convert("RGB")


def add_light_bloom(img):

    overlay = Image.new("RGBA",(WIDTH,HEIGHT),(0,0,0,0))
    d = ImageDraw.Draw(overlay)

    for i in range(3):

        x=random.randint(200,800)
        y=random.randint(200,800)
        r=random.randint(200,400)

        d.ellipse(
            (x-r,y-r,x+r,y+r),
            fill=(255,255,255,30)
        )

    overlay = overlay.filter(ImageFilter.GaussianBlur(120))

    img = Image.alpha_composite(img.convert("RGBA"),overlay)

    return img.convert("RGB")


def draw_quote(img,quote,source):

    draw = ImageDraw.Draw(img)

    font_big = ImageFont.truetype("DejaVuSans-Bold.ttf",64)
    font_small = ImageFont.truetype("DejaVuSans.ttf",36)

    wrapped = textwrap.fill(quote,width=24)

    w,h = draw.multiline_textbbox((0,0),wrapped,font=font_big)[2:]

    x = (WIDTH-w)/2
    y = (HEIGHT-h)/2 - 40

    # shadow
    draw.multiline_text(
        (x+4,y+4),
        wrapped,
        font=font_big,
        fill=(0,0,0),
        align="center"
    )

    # text
    draw.multiline_text(
        (x,y),
        wrapped,
        font=font_big,
        fill=(255,255,255),
        align="center"
    )

    # source
    sw,sh = draw.textbbox((0,0),source,font=font_small)[2:]

    sx = (WIDTH-sw)/2
    sy = y+h+40

    draw.text(
        (sx,sy),
        source,
        font=font_small,
        fill=(255,215,120)
    )

    # accent line
    draw.line(
        (WIDTH*0.2, sy+sh+20, WIDTH*0.8, sy+sh+20),
        fill=(255,215,120),
        width=3
    )


def generate():

    quote,source = random.choice(QUOTES)

    img = cinematic_background()

    img = add_light_bloom(img)

    img = add_vignette(img)

    draw_quote(img,quote,source)

    filename = f"{OUTPUT}/viral_{random.randint(1000,9999)}.png"

    img.save(filename)

    print("generated:",filename)


if __name__ == "__main__":
    generate()
