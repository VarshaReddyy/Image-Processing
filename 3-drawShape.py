import cv2 as cv
import numpy as np
blank =np.zeros((500,500,3), dtype='uint8')
#rectangle
cv.rectangle(blank,(50,50),(200,200),(155,155,0),thickness=2)

cv.arrowedLine(blank,(400,100),(100,400),(100,200,100),thickness=2)
#cv.imshow('rectangle',blank)
#circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),80,(50,200,0),thickness=-1)
#cv.imshow('circle',blank)
#line
cv.line(blank,(blank.shape[1]//2,blank.shape[0]//2),(blank.shape[1],blank.shape[0]),(0,0,255),thickness=2)
#text
cv.putText(blank,'Hello',(200,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),thickness=2)
cv.imshow('line',blank)
cv.waitKey(0)
