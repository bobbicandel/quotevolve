import numpy as np
from PIL import Image
import random

SIZE = 1200


def noise():

    return np.random.rand(SIZE,SIZE)


def rings():

    x = np.linspace(-1,1,SIZE)
    y = np.linspace(-1,1,SIZE)

    X,Y = np.meshgrid(x,y)

    R = np.sqrt(X**2 + Y**2)

    Z = np.sin(R*15)

    return Z


def waves():

    x = np.linspace(0,6*np.pi,SIZE)
    y = np.linspace(0,6*np.pi,SIZE)

    X,Y = np.meshgrid(x,y)

    Z = np.sin(X)+np.cos(Y)

    return Z


def plasma():

    a = rings()
    b = waves()
    c = noise()

    Z = a*0.6 + b*0.3 + c*0.3

    Z = (Z - Z.min())/(Z.max()-Z.min())

    return Z


def palette():

    palettes = [

        ((0,255,255),(0,40,120),(255,0,180)),
        ((255,120,0),(255,0,80),(60,0,140)),
        ((0,255,150),(0,60,255),(10,10,30)),
        ((255,0,120),(255,220,0),(0,0,0)),
        ((0,200,255),(120,0,255),(0,0,0)),

    ]

    return random.choice(palettes)


def generate():

    Z = plasma()

    c1,c2,c3 = palette()

    r = (Z*c1[0] + (1-Z)*c2[0]).astype(np.uint8)
    g = (Z*c1[1] + (1-Z)*c2[1]).astype(np.uint8)
    b = (Z*c1[2] + (1-Z)*c3[2]).astype(np.uint8)

    img = np.stack([r,g,b],axis=2)

    return Image.fromarray(img)
