# prewitt
import cv2
import numpy as np
original_image = cv2.imread('lena.jpg',0)
cv2.imshow('Original Image', original_image)
kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
img_prewittx = cv2.filter2D(original_image, -1, kernelx)
img_prewitty = cv2.filter2D(original_image, -1, kernely)
prewitt = cv2.add(img_prewittx, img_prewitty)
cv2.imshow('prewit', prewitt)
cv2.waitKey(0)



