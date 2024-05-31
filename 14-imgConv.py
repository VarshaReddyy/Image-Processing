"""3.) Using an image show me these using opencv:
     a.) coloured Image to grey image
     b.) Grayscale Image to binary
     c.) Edge detection in a Image"""
import cv2 as cv
img=cv.imread("photos/cat.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("gray",gray)
ret,bin=cv.threshold(gray,70,255,0)
#cv.imshow("binary",bin)
edge=cv.Canny(img,100,500)
cv.imshow("edge",edge)
cv.waitKey(0)
