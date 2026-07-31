import cv2
import numpy as np
image = cv2.imread("lena.jpg")
kernel_size = 3
max_filtered = cv2.dilate(image, np.ones((kernel_size, kernel_size)))
print(max_filtered)
min_filtered = cv2.erode(image, np.ones((kernel_size, kernel_size), np.uint8))
cv2.imshow("o1",max_filtered)
cv2.imshow("o2",min_filtered)
cv2.waitKey(0)