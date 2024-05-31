#Contour properties using opencv
import cv2
import numpy as np

img = cv2.imread("photos/shapes.png")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1,220,255,cv2.THRESH_BINARY_INV)

cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

area1 = []
for c in cnts:
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    area = cv2.contourArea(c)
    area1.append(area)
    
    if area<10000:
        epsilon = 0.01*cv2.arcLength(c,True) #arc lenght take contour and return its perimeter
        data= cv2.approxPolyDP(c,epsilon,True)
        
        hull = cv2.convexHull(data)
        
        x,y,w,h = cv2.boundingRect(hull)
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(125,10,20),5)
 
    # draw the contour and center of the shape on the image
    cv2.drawContours(img, [c], -1, (50, 100, 50), 2)
    cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
from matplotlib import pyplot as plt
titles=["original===","gray==","thresh=="]
images=[img,img1,thresh]
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)