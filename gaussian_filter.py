# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 23:40:48 2021

@author: khan Mustuffa
"""

import random
import cv2

def add_noise(img):

	# Getting the dimensions of the image
	row , col = img.shape
	
	# Randomly pick some pixels in the
	# image for coloring them white
	# Pick a random number between 300 and 10000
	number_of_pixels = random.randint(300, 10000)
	for i in range(number_of_pixels):
		
		# Pick a random y coordinate
		y_coord=random.randint(0, row - 1)
		
		# Pick a random x coordinate
		x_coord=random.randint(0, col - 1)
		
		# Color that pixel to white
		img[y_coord][x_coord] = 255
		
	# Randomly pick some pixels in
	# the image for coloring them black
	# Pick a random number between 300 and 10000
	number_of_pixels = random.randint(300 , 10000)
	for i in range(number_of_pixels):
		
		# Pick a random y coordinate
		y_coord=random.randint(0, row - 1)
		
		# Pick a random x coordinate
		x_coord=random.randint(0, col - 1)
		
		# Color that pixel to black
		img[y_coord][x_coord] = 0
		
	return img

# salt-and-pepper noise can
# be applied only to greyscale images
# Reading the color image in greyscale image
img = cv2.imread('images/pic.jpeg', cv2.IMREAD_GRAYSCALE)

#Storing the image
cv2.imwrite('images/salt-and-pepper-mine.jpg',
			add_noise(img))



#applying now Gaussian filter to denoise
import cv2 as cv
import matplotlib.pyplot as plt
input_img = cv.imread('images/salt-and-pepper-mine.jpg')
gaussian_filtered_pic = cv.GaussianBlur(input_img, (3,3), 0, borderType = cv.BORDER_CONSTANT)
plt.imshow(input_img)
#plt.imshow(gaussian_filtered_pic)
#cv.imwrite('images/gaussian_filtered_pic.jpg', gaussian_filtered_pic)
#Thank You