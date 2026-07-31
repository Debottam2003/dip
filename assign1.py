import cv2
import numpy as np
i = cv2.imread("OIP.jpg")
b, g, r = cv2.split(i)
zeros = np.zeros_like(r)
blue_channel = cv2.merge([b, zeros, zeros])
green_channel = cv2.merge([zeros, g, zeros])
red_channel = cv2.merge([zeros, zeros, r])
print(blue_channel)
print(green_channel)
print(red_channel)
cv2.imshow("blue",blue_channel)
cv2.imshow("green",green_channel)
cv2.imshow("red",red_channel)
cv2.waitKey(0)

