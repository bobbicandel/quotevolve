from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

SIZE = 1200
SAFE = 200


def loadfont(size):

    paths = [
        "fonts/poppins.ttf",
        "fonts/montserrat.ttf",
        "fonts/playfair.ttf"
    ]

    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p,size)

    return ImageFont.load_default()


def wrap(draw,text,font,maxwidth):

    words=text.split()

    lines=[]
    line=""

    for w in words:

        test=line+" "+w if line else w

        box=draw.textbbox((0,0),test,font=font)

        if box[2] <= maxwidth:
            line=test
        else:
            lines.append(line)
            line=w

    if line:
        lines.append(line)

    return lines


def autofont(draw,text):

    for size in range(90,40,-4):

        font=loadfont(size)

        lines=wrap(draw,text,font,SIZE-SAFE*2)

        h=len(lines)*size*1.4

        if h < SIZE*0.55:
            return font,lines

    font=loadfont(48)

    return font,wrap(draw,text,font,SIZE-SAFE*2)


def brightness(img):

    arr=np.array(img.convert("L"))

    return arr.mean()


def textcolor(bg):

    b=brightness(bg)

    if b < 120:
        return (255,255,255)

    return (20,20,20)


def render(bg,quote,source):

    img = bg.resize((SIZE,SIZE)).convert("RGB")

    draw = ImageDraw.Draw(img)

    font,lines = autofont(draw,quote)

    spacing = int(font.size * 1.35)

    textheight = len(lines)*spacing

    y = (SIZE-textheight)/2

    color=textcolor(bg)

    for line in lines:

        box = draw.textbbox((0,0),line,font=font)

        w = box[2]

        x = (SIZE-w)/2

        draw.text(
            (x,y),
            line,
            font=font,
            fill=color,
            stroke_width=3,
            stroke_fill=(0,0,0)
        )

        y += spacing

    small = loadfont(36)

    box = draw.textbbox((0,0),source,font=small)

    w = box[2]

    draw.text(
        ((SIZE-w)/2,y+40),
        source,
        font=small,
        fill=(255,215,0)
    )

    return img
