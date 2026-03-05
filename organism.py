import random
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 1200
HEIGHT = 1200

DATA = [
("Sesungguhnya bersama kesulitan ada kemudahan","QS Al-Insyirah 5-6"),
("Allah tidak membebani seseorang melainkan sesuai kesanggupannya","QS Al-Baqarah 286"),
("Janganlah berputus asa dari rahmat Allah","QS Az-Zumar 53"),
("Sebaik-baik manusia adalah yang paling bermanfaat bagi manusia","HR Bukhari"),
("Allah itu indah dan menyukai keindahan","HR Muslim"),
("Bertakwalah kepada Allah di mana pun kamu berada","HR Tirmidzi"),
]

def nebula():

    img = Image.new("RGB",(WIDTH,HEIGHT))
    px = img.load()

    seed=random.random()*10

    for y in range(HEIGHT):
        for x in range(WIDTH):

            v=(
                math.sin(x*0.012+seed)+
                math.sin(y*0.018+seed)+
                math.sin((x+y)*0.009)+
                math.sin(math.sqrt(x*x+y*y)*0.02)
            )

            v=(v+4)/8

            r=int(30+v*150)
            g=int(40+v*100)
            b=int(120+v*140)

            px[x,y]=(r,g,b)

    img=img.filter(ImageFilter.GaussianBlur(5))

    return img


def glow(img):

    layer=Image.new("RGBA",(WIDTH,HEIGHT),(0,0,0,0))
    d=ImageDraw.Draw(layer)

    for _ in range(6):

        x=random.randint(0,WIDTH)
        y=random.randint(0,HEIGHT)
        r=random.randint(200,400)

        d.ellipse(
            (x-r,y-r,x+r,y+r),
            fill=(255,200,150,40)
        )

    layer=layer.filter(ImageFilter.GaussianBlur(140))

    img=Image.alpha_composite(img.convert("RGBA"),layer)

    return img.convert("RGB")


def card(img):

    overlay=Image.new("RGBA",(WIDTH,HEIGHT),(0,0,0,0))
    d=ImageDraw.Draw(overlay)

    margin=180

    d.rounded_rectangle(
        (margin,margin,WIDTH-margin,HEIGHT-margin),
        radius=60,
        fill=(0,0,0,170)
    )

    img=Image.alpha_composite(img.convert("RGBA"),overlay)

    return img.convert("RGB")


def drawquote(img,quote,source):

    draw=ImageDraw.Draw(img)

    # auto font scaling
    if len(quote) > 80:
        size=58
        wrap=26
    elif len(quote) > 50:
        size=64
        wrap=24
    else:
        size=72
        wrap=22

    font_big=ImageFont.truetype("DejaVuSans-Bold.ttf",size)
    font_small=ImageFont.truetype("DejaVuSans.ttf",38)

    wrapped=textwrap.fill(quote,width=wrap)

    w,h=draw.multiline_textbbox((0,0),wrapped,font=font_big,spacing=16)[2:]

    x=(WIDTH-w)/2
    y=(HEIGHT-h)/2-50

    # shadow stroke
    for dx in [-2,-1,1,2]:
        for dy in [-2,-1,1,2]:

            draw.multiline_text(
                (x+dx,y+dy),
                wrapped,
                font=font_big,
                fill=(0,0,0),
                align="center",
                spacing=16
            )

    draw.multiline_text(
        (x,y),
        wrapped,
        font=font_big,
        fill=(255,255,255),
        align="center",
        spacing=16
    )

    sw,sh=draw.textbbox((0,0),source,font=font_small)[2:]

    sx=(WIDTH-sw)/2
    sy=y+h+40

    draw.text(
        (sx,sy),
        source,
        font=font_small,
        fill=(255,215,120)
    )


def generate():

    quote,source=random.choice(DATA)

    img=nebula()

    img=glow(img)

    img=card(img)

    drawquote(img,quote,source)

    return img
