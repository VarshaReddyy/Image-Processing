#Display the co-ordinates of the points clicked on image using opencv
import cv2 as cv
def coordinate(event,x,y,flag,param):
    if event == cv.EVENT_RBUTTONDOWN:
        coord=". "+str(x)+", "+str(y)
        cv.putText(img,coord,(x,y),1,1,(0,255,0),2)
img = cv.imread("photos/avengers.jpg")
img=cv.resize(img,(500,450))
cv.namedWindow(winname="res")
cv.setMouseCallback("res",coordinate)
while True:
    cv.imshow("res",img)
    if cv.waitKey(1) & 0xFF== 27:
        break
cv.destroyAllWindows()
