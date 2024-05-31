#flip a image horizontally using opencv
import cv2 as cv
import numpy as np

# Read the image
img = cv.imread("photos/abc.jpg")

# Flip the image vertically
flipped_image = np.flipud(img)

# Display the flipped image using Matplotlib
cv.imshow("flipped Image",flipped_image)
cv.waitKey(0)
cv.destroyAllWindows()
