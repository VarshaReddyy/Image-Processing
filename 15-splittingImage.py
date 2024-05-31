#spliting an image using opencv
import cv2 as cv
img=cv.imread("photos/cat.jpg")
b,g,r = cv.split(img)
cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)
cv.waitKey(0)
cv.destroyAllWindows()