import cv2
import numpy as np
# Read the input image
image = cv2.imread('lena.jpg',0)
k = 3
kernel = np.ones((k,k),np.float32) / (k * k)
w = cv2.filter2D(image,-1,kernel)
cv2.imshow("ouput",w)
cv2.waitKey(0)