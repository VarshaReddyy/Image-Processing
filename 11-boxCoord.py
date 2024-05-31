#Draw boxes on Image and also display co-ordinates of box drawn on image
import cv2 as cv 
import numpy as np
def draw(event,x,y,flag,param):
    if event== cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+175,y+175),(125,125,255),2)
        a="("+str(x)+", "+str(y)+")"
        b="("+str(x)+", "+str(y+175)+")"
        c="("+str(x+175)+", "+str(y)+")"
        d="("+str(x+175)+", "+str(y+175)+")"
        cv.putText(img,a,(x,y),1,1.1,(0,255,0),thickness=1)
        cv.putText(img,b,(x,y+175),1,1.1,(0,255,0),thickness=1)
        cv.putText(img,c,(x+175,y),1,1.1,(0,255,0),thickness=1)
        cv.putText(img,d,(x+175,y+175),1,1.1,(0,255,0),thickness=1)
cv.namedWindow(winname="res")
img=np.zeros((500,500,3),np.uint8)
cv.setMouseCallback("res",draw)
while True:
    cv.imshow("res",img)
    if cv.waitKey(1) & 0xFF==27:
        break
cv.destroyAllWindows()