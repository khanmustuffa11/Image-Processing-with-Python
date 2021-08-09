# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 00:43:20 2021

@author: khan Mustuffa
"""
import cv2 as cv
import matplotlib.pyplot as plt
import random


#adding salt and pepper noise to an image
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
# here i have just uploaded locally salt and pepper noise image but you can use above function to add noise to image

img_salt_pepper_noise = cv.imread('images/snp.jpg')
img  = img_salt_pepper_noise
median_output = cv.medianBlur(img,3)  # 3 is kernel size

#plt.imshow(median_output)
#cv.imwrite('images/median_output.jpg',median_output)

cv.imshow("Orginal Image", img)
cv.imshow("median image", median_output)


cv.waitKey(0)
cv.destroyAllwindows()