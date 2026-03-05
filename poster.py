from PIL import Image,ImageDraw,ImageFont,ImageFilter
import textwrap

SIZE = 1200

def wrap(text):

    return "\n".join(textwrap.wrap(text,25))


def glow(draw,xy,text,font):

    x,y = xy

    for r in range(8,0,-2):

        draw.text(
            (x-r,y-r),
            text,
            font=font,
            fill=(255,255,255,40)
        )


def render(bg,quote,source):

    img = bg.resize((SIZE,SIZE)).convert("RGBA")

    overlay = Image.new("RGBA",(SIZE,SIZE),(0,0,0,120))
    img = Image.alpha_composite(img,overlay)

    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf",70)
        small = ImageFont.truetype("DejaVuSans.ttf",36)
    except:
        font = ImageFont.load_default()
        small = ImageFont.load_default()

    text = wrap(quote)

    w,h = draw.multiline_textbbox((0,0),text,font=font)[2:]

    x = (SIZE-w)/2
    y = (SIZE-h)/2

    glow(draw,(x,y),text,font)

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
