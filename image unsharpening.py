# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 23:02:41 2021

@author: khan Mustuffa
"""

#image filtering with python- Unsharp mask
#unsharpened image = original + amount *(original - blurred)

from skimage import io, img_as_float
from skimage.filters import unsharp_mask
from skimage.filters import gaussian
import matplotlib.pyplot as plt


#using manual code to unsharp the image
img = img_as_float(io.imread("images/img.png", as_gray=True)) #reading image
gaussian_img = gaussian(img, sigma =2, mode='constant', cval=0.0) #gaussian filtering
img2 = (img - gaussian_img)*2  #subtracting gaussian from original and and multiplying
img3 = img+img2  #unsharpened image
plt.imshow(img3, cmap = "gray")
##end


#using Unsharp_mask from skimage libaray
#radius defines the degree of blurring
#amount defines the multiplication of factor for (orginal - blurred image)

unsharpened_img = unsharp_mask(img, radius = 3, amount = 2) #applying unsharp mask

fig = plt.figure(figsize = (15,15))
ax1 = fig.add_subplot(1,2,1)
ax1.imshow(img, cmap = 'gray')
ax1.title.set_text('input image')
ax2  =fig.add_subplot(1,2,2)
ax2.imshow(unsharpened_img, cmap = 'gray')
ax2.title.set_text('unsharped image')

plt.show()