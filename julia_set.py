from PIL import Image
from color import *

colors = [WHITE, RED, GREEN, BLUE, ORANGE]
GOLDEN_RATIO = 1.61803
julia_set_options = [complex(0.285, 0.01), complex(
    1-GOLDEN_RATIO, 0), complex(GOLDEN_RATIO - 2, GOLDEN_RATIO - 1), complex(-0.8, 0.156), complex(-0.4, 0.6)]


def is_inside(x, y, iterations, option):
    c = julia_set_options[option]
    z = complex(x, y)
    for i in range(iterations):
        tmp = z.real*z.real - z.imag*z.imag
        zImag = 2 * z.real * z.imag + c.imag
        zReal = tmp + c.real
        z = complex(zReal, zImag)
        if abs(z) >= 2:
            break
    return i/iterations


def make_fractal(ulx, uly, drx, dry, img_width, iterations):
    img_height = int((uly-dry)/(drx-ulx) * img_width)

    print (img_width, img_height)
    im = Image.new("RGB", (img_width, img_height), tuple(BLACK))
    pix = im.load()
    color = colors[4]

    for px in range(img_width):
        for py in range(img_height):
            x = ulx + px/img_width * (drx-ulx)
            y = dry + py/img_height * (uly-dry)
            scalar = is_inside(x, y, iterations, 4)
            pix[px, py] = color.multuple(scalar)

    return im


def default_settings():
    return (-1.5, 1.5, 1.5, -1.5, 512, 150)
