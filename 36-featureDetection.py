#feature detection using harris corner detection, keypoints and SIFT
import cv2
import numpy as np

image_path = 'photos/building.jpg'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define parameters for Harris Corner Detection
block_size = 2
aperture_size = 3
k = 0.04 # Harris detector free parameter

# Detect corners using Harris Corner Detection
corners = cv2.cornerHarris(gray_image, block_size, aperture_size, k)

# Normalize the corners to highlight the strongest ones
corners = cv2.normalize(corners, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Define a threshold to select strong corners
threshold = 150
corner_markers = np.zeros_like(corners)
corner_markers[corners > threshold] = 255

# Initialize SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
keypoints, descriptors = sift.detectAndCompute(gray_image, None)

# Draw keypoints on the image
image_with_keypoints = cv2.drawKeypoints(gray_image, keypoints, image, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display images
cv2.imshow('Corners', corner_markers)
cv2.imshow('Keypoints', image_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()