#Display the pixel colour of the points clicked on image using OpenCV
import cv2 as cv 
def pixelColour(event,x,y,flag,param):
    if event == cv.EVENT_RBUTTONDOWN:
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        color_bgr=". "+str(b)+', '+str(g)+', '+str(r)
        cv.putText(img,color_bgr,(x,y),1,1,(100,125,100),2)
img=cv.imread('photos/car.jpg')
img= cv.resize(img,(500,450))
cv.namedWindow(winname="res")
cv.setMouseCallback("res",pixelColour)
while True:
    cv.imshow("res",img)
    if cv.waitKey(1) & 0xFF== 27:
        break
cv.destroyAllWindows()