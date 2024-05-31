#object detection using HSV color space
import numpy as np
import cv2 as cv
frame=cv.imread('photos/colorBalls3.jpg')
while True:
    hsv= cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    u_v=np.array([52,250,240])
    l_v=np.array([38,168,162])
    #creating mask
    mask= cv.inRange(hsv,l_v,u_v)
    #filter mask with image
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow("frame",frame)
    cv.imshow("mask",mask)
    cv.imshow("res",res)
    k=cv.waitKey(1)
    if k==27:
        break
cv.destroyAllWindows()