from PIL import Image,ImageDraw,ImageFont,ImageFilter
import numpy as np
import random
import os

SIZE = 1200
SAFE = 180


def brightness(img):

    arr = np.array(img.convert("L"))
    return arr.mean()


def font():

    fonts=[
        "fonts/poppins.ttf",
        "fonts/montserrat.ttf",
        "fonts/playfair.ttf"
    ]

    for f in fonts:
        if os.path.exists(f):
            return ImageFont.truetype(f,72)

    return ImageFont.load_default()


def smallfont():

    fonts=[
        "fonts/poppins.ttf",
        "fonts/montserrat.ttf"
    ]

    for f in fonts:
        if os.path.exists(f):
            return ImageFont.truetype(f,36)

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

    return "\n".join(lines)


def choosecolor(bg):

    b=brightness(bg)

    if b < 80:
        return (255,255,255)

    if b < 140:
        return (255,215,0)

    return (20,20,20)


def glow(draw,x,y,text,font):

    for g in range(12,0,-2):

        draw.multiline_text(
            (x-g,y-g),
            text,
            font=font,
            fill=(0,0,0,35),
            align="center"
        )


def score(img):

    arr=np.array(img.convert("L"))

    contrast=arr.std()

    return contrast


def layout(bg,quote,source,mode):

    img = bg.resize((SIZE,SIZE)).convert("RGBA")

    overlay = Image.new("RGBA",(SIZE,SIZE),(0,0,0,110))
    img = Image.alpha_composite(img,overlay)

    draw = ImageDraw.Draw(img)

    f=font()
    sf=smallfont()

    maxwidth=SIZE-SAFE*2

    text=wrap(draw,quote,f,maxwidth)

    box=draw.multiline_textbbox((0,0),text,font=f)

    w=box[2]
    h=box[3]

    if mode=="center":
        y=(SIZE-h)/2
    elif mode=="top":
        y=SIZE*0.25
    else:
        y=SIZE*0.65-h

    x=(SIZE-w)/2

    c=choosecolor(bg)

    glow(draw,x,y,text,f)

    draw.multiline_text(
        (x,y),
        text,
        font=f,
        fill=c,
        align="center"
    )

    sw,sh=draw.textbbox((0,0),source,font=sf)[2:]

    draw.text(
        ((SIZE-sw)/2,y+h+50),
        source,
        font=sf,
        fill=(255,215,0)
    )

    img=img.filter(ImageFilter.SMOOTH)

    return img


def render(bg,quote,source):

    modes=["center","top","bottom"]

    best=None
    bestscore=-1

    for m in modes:

        img=layout(bg,quote,source,m)

        s=score(img)

        if s>bestscore:
            bestscore=s
            best=img

    return best.convert("RGB")
