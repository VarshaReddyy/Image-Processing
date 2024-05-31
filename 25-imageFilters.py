#Image Smoothing using filters - homogeneous,blur(averaging),gaussian,median,bilateral
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread("photos/noisy.jpg")  
img = cv2.resize(img,(400,400))

kernel = np.ones((5,5),np.float32)/25

#FILTER NUMBER -----1 
h_filter = cv2.filter2D(img,-1,kernel) 

#FILtER NUMBER 2-----
blur = cv2.blur(img,(8,8))

#Filter Number 3------
gau= cv2.GaussianBlur(img,(5,5),0) #here 0 is sigma x value

#Filter Number 4--

med = cv2.medianBlur(img,5)

#bilateral filter --
bi_f = cv2.bilateralFilter(img,9,75,75)

titles = ["original_image","homo","blur","gauss","med","bi_f"]
images = [img,h_filter,blur,gau,med,bi_f]

for i in range(6):
    plt.subplot(2, 3, i+1), 
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()