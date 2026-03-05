import random
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 1200
HEIGHT = 1200

QUOTES = [
("Allah tidak membebani seseorang melainkan sesuai dengan kesanggupannya","QS Al-Baqarah 286"),
("Sesungguhnya bersama kesulitan ada kemudahan","QS Al-Insyirah 6"),
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
                math.sin((x+y)*0.01)+
                math.sin(math.sqrt(x*x+y*y)*0.02)
            )

            v=(v+4)/8

            r=int(20+v*150)
            g=int(30+v*90)
            b=int(120+v*150)

            px[x,y]=(r,g,b)

    img=img.filter(ImageFilter.GaussianBlur(5))

    return img


def energy(img):

    layer=Image.new("RGBA",(WIDTH,HEIGHT),(0,0,0,0))
    d=ImageDraw.Draw(layer)

    for i in range(6):

        x=random.randint(0,WIDTH)
        y=random.randint(0,HEIGHT)
        r=random.randint(200,500)

        color=random.choice([
            (255,200,120,40),
            (120,200,255,40),
            (255,120,200,40)
        ])

        d.ellipse((x-r,y-r,x+r,y+r),color)

    layer=layer.filter(ImageFilter.GaussianBlur(140))

    img=Image.alpha_composite(img.convert("RGBA"),layer)

    return img.convert("RGB")


def vignette(img):

    overlay=Image.new("RGBA",(WIDTH,HEIGHT),(0,0,0,0))
    d=ImageDraw.Draw(overlay)

    for i in range(400):

        a=int(i*0.45)

        d.rectangle(
            (i,i,WIDTH-i,HEIGHT-i),
            outline=(0,0,0,a)
        )

    img=Image.alpha_composite(img.convert("RGBA"),overlay)

    return img.convert("RGB")


def card(img):

    overlay=Image.new("RGBA",(WIDTH,HEIGHT),(0,0,0,0))
    d=ImageDraw.Draw(overlay)

    m=160

    d.rounded_rectangle(
        (m,m,WIDTH-m,HEIGHT-m),
        radius=50,
        fill=(0,0,0,170)
    )

    img=Image.alpha_composite(img.convert("RGBA"),overlay)

    return img.convert("RGB")


def text(img,quote,source):

    draw=ImageDraw.Draw(img)

    font_big=ImageFont.truetype("DejaVuSans-Bold.ttf",72)
    font_small=ImageFont.truetype("DejaVuSans.ttf",38)

    wrapped=textwrap.fill(quote,width=22)

    w,h=draw.multiline_textbbox((0,0),wrapped,font=font_big)[2:]

    x=(WIDTH-w)/2
    y=(HEIGHT-h)/2-60

    # stroke
    for dx in [-3,-2,-1,1,2,3]:
        for dy in [-3,-2,-1,1,2,3]:

            draw.multiline_text(
                (x+dx,y+dy),
                wrapped,
                font=font_big,
                fill=(0,0,0),
                align="center",
                spacing=12
            )

    draw.multiline_text(
        (x,y),
        wrapped,
        font=font_big,
        fill=(255,255,255),
        align="center",
        spacing=12
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

    draw.line(
        (WIDTH*0.35,sy+sh+20,WIDTH*0.65,sy+sh+20),
        fill=(255,215,120),
        width=4
    )


def generate():

    quote,source=random.choice(QUOTES)

    img=nebula()

    img=energy(img)

    img=vignette(img)

    img=card(img)

    text(img,quote,source)

    return img
