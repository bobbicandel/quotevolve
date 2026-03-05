from PIL import Image,ImageDraw,ImageFont,ImageFilter

SIZE = 1200
SAFE = 200


def wrap(draw,text,font,maxwidth):

    words = text.split()

    lines=[]
    line=""

    for w in words:

        test=line+" "+w if line else w

        box=draw.textbbox((0,0),test,font=font)
        width=box[2]

        if width<=maxwidth:
            line=test
        else:
            lines.append(line)
            line=w

    if line:
        lines.append(line)

    return "\n".join(lines)


def glow(draw,x,y,text,font):

    for g in range(8,0,-2):

        draw.multiline_text(
            (x-g,y-g),
            text,
            font=font,
            fill=(255,255,255,30),
            align="center"
        )


def render(bg,quote,source):

    img = bg.resize((SIZE,SIZE)).convert("RGBA")

    overlay = Image.new("RGBA",(SIZE,SIZE),(0,0,0,130))
    img = Image.alpha_composite(img,overlay)

    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf",70)
        small = ImageFont.truetype("DejaVuSans.ttf",36)
    except:
        font = ImageFont.load_default()
        small = ImageFont.load_default()

    maxwidth = SIZE-SAFE*2

    text = wrap(draw,quote,font,maxwidth)

    box = draw.multiline_textbbox((0,0),text,font=font)

    w = box[2]
    h = box[3]

    x = (SIZE-w)/2
    y = (SIZE-h)/2

    glow(draw,x,y,text,font)

    draw.multiline_text(
        (x,y),
        text,
        font=font,
        fill=(255,255,255),
        align="center"
    )

    sw,sh = draw.textbbox((0,0),source,font=small)[2:]

    draw.text(
        ((SIZE-sw)/2,y+h+60),
        source,
        font=small,
        fill=(255,215,0)
    )

    img = img.filter(ImageFilter.SMOOTH)

    return img.convert("RGB")
