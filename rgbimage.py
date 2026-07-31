import cv2
import numpy as np
i = cv2.imread("lena.jpg")
img = i.copy()
IMG_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
img[:,:,0]=0
img[:,:,1]=0
cv2.imshow("red",img)
print(img)
img = i.copy()
img[:,:,0]=0
img[:,:,2]=0
cv2.imshow("green",img)
print(img)
img = i.copy()
img[:,:,2]=0
img[:,:,1]=0
cv2.imshow("blue",img)
print(img)
cv2.waitKey(0)
