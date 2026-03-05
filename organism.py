import numpy as np
from PIL import Image
import random

SIZE = 1200

def fractal():

    x = np.linspace(-2,2,SIZE)
    y = np.linspace(-2,2,SIZE)

    X,Y = np.meshgrid(x,y)

    Z = (
        np.sin(X*3)
        + np.cos(Y*3)
        + np.sin((X**2+Y**2)*4)
        + np.cos((X**2-Y**2)*2)
    )

    Z = (Z - Z.min())/(Z.max()-Z.min())

    return Z


def palette():

    palettes = [
        ((0,255,255),(255,0,200)),
        ((255,80,0),(255,220,0)),
        ((0,200,255),(120,0,255)),
        ((0,255,120),(0,60,255)),
        ((255,0,120),(255,255,0))
    ]

    return random.choice(palettes)


def generate():

    Z = fractal()

    c1,c2 = palette()

    r = (Z*c1[0] + (1-Z)*c2[0]).astype(np.uint8)
    g = (Z*c1[1] + (1-Z)*c2[1]).astype(np.uint8)
    b = (Z*c1[2] + (1-Z)*c2[2]).astype(np.uint8)

    img = np.stack([r,g,b],axis=2)

    return Image.fromarray(img)
