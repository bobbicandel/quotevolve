import numpy as np
from PIL import Image
import random

SIZE = 1200

def plasma():

    w = SIZE
    h = SIZE

    data = np.zeros((h, w))

    scale = random.uniform(1.5,4)

    for y in range(h):
        for x in range(w):

            nx = x/w - 0.5
            ny = y/h - 0.5

            v = (
                np.sin(nx*scale*10)
                + np.cos(ny*scale*10)
                + np.sin((nx*nx+ny*ny)*scale*20)
            )

            data[y,x] = v

    data = (data - data.min())/(data.max()-data.min())

    return data


def palette():

    palettes = [
        ((0,255,255),(255,0,255),(0,0,255)),
        ((255,140,0),(255,0,150),(0,0,0)),
        ((0,255,120),(0,60,255),(0,0,0)),
        ((255,0,80),(255,220,0),(20,20,20)),
        ((0,200,255),(255,0,120),(10,10,30))
    ]

    return random.choice(palettes)


def generate():

    p = plasma()

    c1,c2,c3 = palette()

    r = (p*c1[0] + (1-p)*c2[0]).astype(np.uint8)
    g = (p*c1[1] + (1-p)*c2[1]).astype(np.uint8)
    b = (p*c1[2] + (1-p)*c3[2]).astype(np.uint8)

    img = np.stack([r,g,b],axis=2)

    return Image.fromarray(img)
