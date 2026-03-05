import numpy as np
from PIL import Image
import random
import os

SIZE = 1200

def generate():

    x = np.linspace(-3,3,SIZE)
    y = np.linspace(-3,3,SIZE)

    X,Y = np.meshgrid(x,y)

    Z = np.sin(X*random.uniform(2,6)) + np.cos(Y*random.uniform(2,6))
    Z += np.sin((X**2+Y**2)*random.uniform(0.5,2))

    Z = (Z - Z.min())/(Z.max()-Z.min())

    r = (np.sin(Z*3.14)*255).astype(np.uint8)
    g = (np.cos(Z*3.14)*255).astype(np.uint8)
    b = (np.sin(Z*6.28)*255).astype(np.uint8)

    img = np.stack([r,g,b],axis=2)

    return Image.fromarray(img)
