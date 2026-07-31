import cv2
import numpy as np
img = cv2.imread("lena.jpg")
i = img.copy()
img[:,:,0] = 0  #blue color removed
cv2.imshow("-blue",img)
print(img)
img = i.copy()
img[:,:,1] = 0  #green color removed
cv2.imshow("-green",img)
print(img)
img = i.copy()
img[:,:,2] = 0  #red color removed
cv2.imshow("-red",img)
print(img)
