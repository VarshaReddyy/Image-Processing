#object detection in live video using trackbars and HSV color space
import numpy as np
import cv2 as cv
cap=cv.VideoCapture(0,cv.CAP_DSHOW)

def nothing(x):
    pass

cv.namedWindow("Color Adjustments")
cv.createTrackbar("Lower_H","Color Adjustments",0,255,nothing )
cv.createTrackbar("Lower_S","Color Adjustments",0,255,nothing )
cv.createTrackbar("Lower_V","Color Adjustments",0,255,nothing )
cv.createTrackbar("Upper_H","Color Adjustments",0,255,nothing )
cv.createTrackbar("Upper_S","Color Adjustments",0,255,nothing )
cv.createTrackbar("Upper_V","Color Adjustments",0,255,nothing )

while True:
    _,frame=cap.read()
    frame =cv.resize(frame, (400,400))
    hsv =cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h=cv.getTrackbarPos("Lower_H", "Color Adjustments")
    l_s=cv.getTrackbarPos("Lower_S", "Color Adjustments")
    l_v=cv.getTrackbarPos("Lower_V", "Color Adjustments")
    u_h=cv.getTrackbarPos("Upper_H", "Color Adjustments")
    u_s=cv.getTrackbarPos("Upper_S","Color Adjustments")
    u_v=cv.getTrackbarPos("Upper_V","Color Adjustments")
    
    lower_bound = np.array([l_h,l_s,l_v])
    upper_bound = np.array([u_h,u_s,u_v])

    mask=cv.inRange(hsv,lower_bound,upper_bound)
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow("Original Frame",frame)
    cv.imshow("Masking",mask)
    cv.imshow("Result",res)
    key=cv.waitKey(25) &0xFF
    if key==27:
        break
cap.release()
cv.destroyAllWindows()