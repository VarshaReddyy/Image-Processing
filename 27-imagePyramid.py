# image pyramid using opencv
import cv2
import numpy as np

img = cv2.imread("photos/cat.jpg")
img = cv2.resize(img,(400,400))

pd1 = cv2.pyrDown(img)
pd2 = cv2.pyrDown(pd1)

pu1 = cv2.pyrUp(pd2)
pu2 = cv2.pyrUp(pu1)

cv2.imshow("original==",img)
cv2.imshow("pd1==",pd1)
cv2.imshow("pd2==",pd2)
cv2.imshow("pu1==",pu1)
cv2.imshow("pu2==",pu2)

cv2.waitKey(0)
cv2.destroyAllWindows()