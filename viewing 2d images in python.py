# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 15:37:41 2021

@author: khan Mustuffa
"""

from skimage import io
img = io.imread('images/pic.jpeg')  #reading images using skimage
io.imshow(img)  #displaying image 

img_gray = io.imread('images/pic.jpeg', as_gray =True)
import matplotlib.pyplot as plt
#plt.imshow(img_gray)
#plt.imshow(img_gray, cmap='Blues')  # displaying images using matplot lib

fig  = plt.figure(figsize =(10,10))

ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img_gray, cmap ='hot')
ax1.title.set_text('ist')

ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img_gray, cmap ='jet')
ax2.title.set_text('2nd')

ax3 = fig.add_subplot(2,2,3)
ax3.imshow(img_gray, cmap ='gray')
ax3.title.set_text('3rd')

ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img_gray, cmap ='nipy_spectral')
ax4.title.set_text('4th')

plt.show()