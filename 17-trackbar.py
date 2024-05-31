#Using the track bar position values, a rectangle is drawn with the fill colour corresponding to RGB colour value.
import cv2 as cv
import numpy as np
img= np.zeros((300,400,3),np.uint8)
cv.namedWindow('image')
def nothing(x):
    pass
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
while(1):
    cv.imshow('image',img)
    k=cv.waitKey(1) & 0xFF
    if k==27:
        break
    r=cv.getTrackbarPos('R','image')
    g=cv.getTrackbarPos('G','image')
    b=cv.getTrackbarPos('B','image')
    cv.rectangle(img, (100,100),(200,200), (b,g,r),-1)
cv.destroyAllWindows()