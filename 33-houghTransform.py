#Circle detection using opencv and HoughCircle
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('photos/col_balls.jpg')
img2= img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,param1=50, param2=30, minRadius=0,maxRadius=0)
data = np.uint16(np.around(circles))
for (x, y ,r) in data[0, :]:
    cv2.circle(img2, (x, y), r, (50, 10, 50), 3) #outer circle
    cv2.circle(img2, (x, y), 2, (0, 255, 100), -1) #center
cv2.imshow("original",img)
cv2.imshow("result",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()