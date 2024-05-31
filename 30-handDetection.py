#hand detection using contour in opencv
import cv2
import numpy as np

img = cv2.imread("photos/hand.jpg")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(img1,11)
ret,thresh = cv2.threshold(blur,240,255,cv2.THRESH_BINARY_INV)
dilata = cv2.dilate(thresh,(1,1),iterations = 6)
cnts,hier = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# loop over the contours
for c in cnts:
    epsilon = 0.0001*cv2.arcLength(c,True)
    data= cv2.approxPolyDP(c,epsilon,True)
    
    hull = cv2.convexHull(data)
    
    
    cv2.drawContours(img, [c], -1, (50, 50, 150), 2)
    cv2.drawContours(img, [hull], -1, (0, 255, 0), 2)

hull2 = cv2.convexHull(cnts[0],returnPoints = False)
defect = cv2.convexityDefects(cnts[0],hull2)

for i in range(defect.shape[0]):
    s,e,f,d = defect[i,0]
    start = tuple(c[s][0])
    end = tuple(c[e][0])
    far = tuple(c[f][0])
    #cv2.line(img,start,end,[255,0,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)
c_max = max(cnts, key=cv2.contourArea)

# determine the most extreme points along the contour
extLeft = tuple(c_max[c_max[:, :, 0].argmin()][0])
extRight = tuple(c_max[c_max[:, :, 0].argmax()][0])
extTop = tuple(c_max[c_max[:, :, 1].argmin()][0])
extBot = tuple(c_max[c_max[:, :, 1].argmax()][0])

cv2.circle(img, extLeft, 8, (255, 0, 255), -1)  #pink
cv2.circle(img, extRight, 8, (0, 125, 255), -1) #brown
cv2.circle(img, extTop, 8, (255, 10, 0), -1)  #blue
cv2.circle(img, extBot, 8, (19, 152, 152), -1) #green
from matplotlib import pyplot as plt
titles=["convexhull","gray","thresh"]
images=[img,img1,thresh]
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()