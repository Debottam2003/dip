import cv2
import numpy as np
img1 = cv2.imread("lena.jpg")
img_clock = cv2.rotate(img1,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("clock",img_clock)
img_anticlock = cv2.rotate(img1,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("anticlock",img_anticlock)
