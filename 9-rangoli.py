#Drawing with mouse and erasing it using mouse event binding and OpenCV
import cv2 as cv
import numpy as np
run=False
color=False
def draw(event,x,y,flag,param):
    global run,color
    if event==cv.EVENT_LBUTTONDOWN:
        run=True
        color=True
        cv.circle(blank,(x,y),5,(255,255,255),-1)
    if event==cv.EVENT_LBUTTONUP:
        run=False
    elif event==cv.EVENT_RBUTTONDOWN:
        run=True
        color=False
        cv.circle(blank,(x,y),5,(0,0,0),-1)
    elif event ==cv.EVENT_RBUTTONUP:
        run=False
    
    elif event==cv.EVENT_MOUSEMOVE:
        if run==True & color==True:
            cv.circle(blank,(x,y),5,(255,255,255),-1)
        elif run==True & color==False:
            cv.circle(blank,(x,y),5,(0,0,0),-1)
cv.namedWindow(winname="rangoli")
blank = np.zeros((500,500,3),np.uint8)
cv.setMouseCallback("rangoli",draw)
while True:
    cv.imshow("rangoli",blank)
    if cv.waitKey(1) & 0xFF==27:
        break
cv.destroyAllWindows()


