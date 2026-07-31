# sobel
import cv2
import numpy as np
original_image = cv2.imread('lena.jpg',0)
cv2.imshow('Original Image', original_image)
kernelx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
kernely = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
img_sobelx = cv2.filter2D(original_image, -1, kernelx)
img_sobely = cv2.filter2D(original_image, -1, kernely)
sobel = cv2.add(img_sobelx, img_sobely)
cv2.imshow('sobel', sobel)
cv2.waitKey(0)



