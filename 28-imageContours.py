#image contours using opencv
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("photos/logo.jpg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img1,127,255,0)

cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(img,cnts,-1,(176,10,15),4)
titles = ["original","gray","thresh"]
images = [img,img1,thresh]
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()