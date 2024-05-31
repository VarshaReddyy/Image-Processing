#image gradient and edge detection using opencv
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("photos/building.jpg")
img = cv2.resize(img,(400,300))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Laplacian Derivative---
lap = cv2.Laplacian(img_gray,cv2.CV_64F,ksize = 3) #also pass kernal size
lap = np.uint8(np.absolute(lap))

#Sobel operation - 
#Sobel X focus on vertical lines
#Sobel y focus on horizontal lines

sobelX = cv2.Sobel(img_gray,cv2.CV_64F,1,0,ksize = 3) #here 1 means x direction
sobelY = cv2.Sobel(img_gray,cv2.CV_64F,0,1,ksize = 3) #here 1 means y direction

sobelX = np.uint8(np.absolute(sobelX))
sobelY= np.uint8(np.absolute(sobelY))

sobelcombine = cv2.bitwise_or(sobelX,sobelY)


titles = ["original","gray","laplacian","sobelX","sobelY","combined"]
images = [img,img_gray,lap,sobelX,sobelY,sobelcombine]

for i in range(6):
    plt.subplot(2,3, i+1), 
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()