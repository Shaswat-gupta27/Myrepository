# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:24:14 2020

@author: Shashwat
"""

from PIL import Image

img =Image.open(r'C:\Users\Shashwat\Pictures\Screenshots\fliped.png')

transpose_img= img.transpose(Image.FLIP_LEFT_RIGHT)

transpose_img.save(r'C:\Users\Shashwat\Pictures\Screenshots\newss.png')
print("done")