#morphological operations (EROSION,DILATION, OPENING, CLOSING) on image using opencv
import cv2
import numpy as np

img = cv2.imread('photos/finger_print.png',0)
_,mask= cv2.threshold(img,230,255,cv2.THRESH_BINARY)
kernel = np.ones((2,2),np.uint8)
e = cv2.erode(mask,kernel)

kernel = np.ones((3,3),np.uint8)
d = cv2.dilate(mask,kernel) 

kernel = np.ones((3,3),np.uint8)
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

kernel = np.ones((3,3),np.uint8)
c= cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel) 

from matplotlib import pyplot as plt
titles = ["img","mask","erosion","dilation","opening","closing"]
images = [img,mask,e,d,o,c]
for i in range(6):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()