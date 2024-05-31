#Draw an equilateral triangle and display co-ordinates of centroid using opencv
import numpy as np
import cv2 as cv
img=np.zeros((300,400,3),np.uint8)
p1 = (100, 200) 
p2 = (50, 50)
p3 = (300, 100) 
cv.line(img,p1,p2,(255,0,0),3)
cv.line(img,p2,p3,(255,0,0),3)
cv.line(img,p3,p1,(255,0,0),3)
centroid=((p1[0]+p2[0]+p3[0])//3,(p1[1]+p2[1]+p3[1])//3)
cv.circle(img,centroid,3,(0,255,0),0)
cv.imshow("triange",img)
cv.waitKey(0)