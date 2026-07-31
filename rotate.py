import cv2
import numpy as np
img = cv2.imread("lena.jpg",0)
cv2.imshow("input",img)

clock = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
anticlock = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("output1",clock)
cv2.imshow("output2",anticlock)

