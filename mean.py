import cv2
import numpy as np
i = cv2.imread("salt_pepper_noise_image.jpg")
kernal = int(input("Enter kernal size:"))
# j = cv2.blur(i,(kernal,kernal))
# cv2.imshow("output",j)
k = cv2.medianBlur(i,kernal)
cv2.imshow("input",i)
cv2.imshow("output",k)
cv2.waitKey(0)