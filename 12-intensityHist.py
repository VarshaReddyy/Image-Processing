#computes histogram for each channel in the image (lena.jpg) and plots the intensity distribution for each channel 
import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt 
img=cv.imread("photos/dog.jpg")
color=('b','g','r')
for i,col in enumerate(color):
   hist = cv.calcHist([img],[i],None,[256],[0,256])
   plt.plot(hist, color = col)
   plt.xlim([0,256])
plt.show()

