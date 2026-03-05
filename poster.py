from PIL import Image,ImageDraw,ImageFont,ImageFilter

SIZE = 1200

def render(background,quote,source):

    img = background.resize((SIZE,SIZE))

    overlay = Image.new("RGBA",(SIZE,SIZE),(0,0,0,120))
    img = Image.alpha_composite(img.convert("RGBA"),overlay)

    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf",60)
        small = ImageFont.truetype("DejaVuSans.ttf",36)
    except:
        font = ImageFont.load_default()
        small = ImageFont.load_default()

    text = quote

    w,h = draw.multiline_textsize(text,font=font)

    x = (SIZE-w)/2
    y = (SIZE-h)/2

    draw.multiline_text(
        (x,y),
        text,
        font=font,
        fill=(255,255,255),
        align="center"
    )

    sw,sh = draw.textsize(source,font=small)

    draw.text(
        ((SIZE-sw)/2,y+h+40),
        source,
        font=small,
        fill=(255,215,0)
    )

    img = img.filter(ImageFilter.SMOOTH)

    return img.convert("RGB")
