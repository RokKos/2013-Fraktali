from PIL import Image
from color import *

iterations = 50
color = Color(255, 128, 0)

def is_inside(x, y):
    c = complex(x, y)
    z = 0
    for i in range(iterations):
        z *= z
        z += c
        if abs(z) >= 2:
            break
    return i/iterations

def make_fractal(ulx, uly, drx, dry, img_width):
    img_height = int((uly-dry)/(drx-ulx) * img_width)
    print (img_width,img_height)
    im = Image.new("RGB",(img_width,img_height),tuple(BLACK))
    pix = im.load()

    for px in range(img_width):
        for py in range(img_height):
            x = ulx + px/img_width * (drx-ulx)
            y = dry + py/img_height * (uly-dry)
            scalar = is_inside(x,y)
            pix[px,py] = color.multuple(scalar)

    return im

def default_settings():
    return (-2.2,1.2,0.7,-1.2,400)
