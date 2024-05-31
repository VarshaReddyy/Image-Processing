import cv2 as cv
import numpy as np
def draw(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),60,(125,0,255),3)
    elif event==cv.EVENT_RBUTTONDBLCLK:
        cv.rectangle(img,(x,y),(x+75,y+75),(125,125,255),2)
cv.namedWindow(winname="res")
img=np.zeros((500,500,3),np.uint8)
cv.setMouseCallback("res",draw)
while True:
    cv.imshow("res",img)
    if cv.waitKey(1) & 0xFF== 27:
        break
cv.destroyAllWindows()