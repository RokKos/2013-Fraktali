# -*- coding: utf-8 -*-

from PIL import Image
import numpy

# Naredimo random array vrednosti od 0-255 dimenzij 800x800x3 in spremenimo tip
# na uint8 (to je en byte, toliko rabimo za opis barve, od 0 - 255).
# S tem torej naredimo sliko velikosti 800x800 pikslov, ki ima RGB barve. Če bi
# želeli RGBA (še transparentnost) bi naredili array velikosti 800x800x4
array = numpy.uint8(numpy.random.randint(0, 255, size=(800, 800, 3)))

# array laho naredimo tudi tako, da spremenimo pythonov list
# a = numpy.array(
#     [[[0, 0, 255], [0, 0, 255]], [[0, 0, 255], [0, 0, 255]]],
#     dtype=numpy.uint8
# )

#naredimo sliko in jo pokažemo
img = Image.fromarray(array, 'RGB')
img.show()


#### ALI ####

from PIL import Image
from random import randint

img = Image.new( 'RGB', (255,255), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (i,0,i) # set the colour accordingly
 
img.save(r'C:\Users\bajecklemen\Desktop\image6.png')
