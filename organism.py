import random
import numpy as np
from PIL import Image, ImageFilter

W = 1200
H = 1200


def gradient():

    img = np.zeros((H, W, 3), dtype=np.float32)

    c1 = np.array([
        random.randint(40,90),
        random.randint(60,120),
        random.randint(120,200)
    ])

    c2 = np.array([
        random.randint(120,200),
        random.randint(80,150),
        random.randint(60,120)
    ])

    for y in range(H):

        ty = y / H

        for x in range(W):

            tx = x / W

            mix = (tx + ty) / 2

            color = (1-mix)*c1 + mix*c2

            img[y,x] = color

    return img


def plasma(img):

    for _ in range(6):

        cx = random.randint(0, W)
        cy = random.randint(0, H)

        radius = random.randint(200,500)

        for y in range(H):

            for x in range(W):

                dx = x - cx
                dy = y - cy

                d = (dx*dx + dy*dy) ** 0.5

                if d < radius:

                    glow = (1 - d/radius) * random.randint(30,60)

                    img[y,x] += glow

    return np.clip(img,0,255)


def grain(img):

    noise = np.random.normal(0,7,(H,W,3))

    img = img + noise

    return np.clip(img,0,255)


def vignette(img):

    cx = W/2
    cy = H/2

    maxd = (cx**2 + cy**2)**0.5

    for y in range(H):

        for x in range(W):

            d = ((x-cx)**2 + (y-cy)**2)**0.5

            v = d / maxd

            img[y,x] *= (1 - v*0.35)

    return np.clip(img,0,255)


def generate():

    img = gradient()

    img = plasma(img)

    img = grain(img)

    img = vignette(img)

    img = img.astype("uint8")

    im = Image.fromarray(img)

    im = im.filter(ImageFilter.GaussianBlur(0.6))

    return im
