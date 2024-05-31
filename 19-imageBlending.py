#image blending using opencv
import numpy as np
import cv2 as cv
img1=cv.imread('photos/abc.jpg')
cv.resize(img1,(500,500))
img2=cv.imread('photos/xyz.jpg')
cv.resize(img2,(500,500))
cv.imshow("img1",img1)
cv.imshow("img2",img2)
result=cv.addWeighted(img1,0.5,img2,0.5,0)
cv.imshow("result",result)
cv.waitKey(0)
cv.destroyAllWindows()