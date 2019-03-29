#!/usr/bin/env python3

# resizes all images in current working directory to fit 300x300 square
# and adds catlogo.png to lower-right corner

import os
from PIL import Image

sqFitSize = 300
logoFile = 'catlogo.png'

logoIm = Image.open(logoFile)
logoWidth, logoHeight = logoIm.size

# loop over all the image files in current working directory

for fileName in os.listdir('.'):
    if not (fileName.endswith('.png') or fileName.endswith('.jpg')) \
        or fileName == logoFile:
        continue # skips non-image files and the logo file itself
    
    im =Image.open(fileName)
    width, height = im.sqFitSize

    # chk if image requires resizing

    if width > height:
        height = int((sqFitSize/width)*height)
        width = sqFitSize
    else:
        width = int((sqFitSize/height)*width)
        height = sqFitSize
    
    #resize the image

    print('Resizing %s...' %(fileName))
    im = im.resize((width,height))

    # add the logo to lower right corner
    print('Adding logo to %s...' %(fileName))
    im.paste(logoIm,(width - logoWidth, height - logoHeight), logoIm)

    #save changes
    im.save(os.path.join('withLogo'), fileName)
