import random
import numpy as np
from PIL import Image, ImageFilter


W = 1200
H = 1200


def cosmic_gradient():

    base = np.zeros((H, W, 3), dtype=np.float32)

    c1 = np.array([
        random.randint(20,60),
        random.randint(40,90),
        random.randint(80,160)
    ])

    c2 = np.array([
        random.randint(120,180),
        random.randint(80,140),
        random.randint(60,120)
    ])

    for y in range(H):

        t = y / H

        color = (1-t)*c1 + t*c2

        base[y,:,:] = color

    return base


def grain_texture(img):

    noise = np.random.normal(0, 8, (H, W, 3))

    img = img + noise

    return np.clip(img,0,255)


def fractal_light(img):

    for _ in range(8):

        cx = random.randint(0, W)
        cy = random.randint(0, H)

        radius = random.randint(150,400)

        for y in range(H):

            for x in range(W):

                dx = x - cx
                dy = y - cy

                d = (dx*dx + dy*dy)**0.5

                if d < radius:

                    glow = (1 - d/radius) * 40

                    img[y,x] += glow

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

    img = cosmic_gradient()

    img = grain_texture(img)

    img = fractal_light(img)

    img = vignette(img)

    img = img.astype("uint8")

    im = Image.fromarray(img)

    im = im.filter(ImageFilter.SMOOTH)

    return im
