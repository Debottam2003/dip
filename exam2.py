import cv2
import numpy as np
img1 = cv2.imread("lena.jpg")
img2 = img1.copy()
img=(255-img1)
cv2.imshow("res",img1)
img_color = cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)
cv2.imshow("2",img_color)
img1 = img2.copy()
IMG_YCRCB = cv2.cvtColor(img1,cv2.COLOR_RGB2YCrCb)
cv2.imshow("3",IMG_YCRCB)
IMG_HSV = img1 = img2.copy()
IMG_HSV = cv2.cvtColor(img1,cv2.COLOR_RGB2HSV)
cv2.imshow("4",IMG_HSV)
cv2.imshow("5",img)
_,BINARY = cv2.threshold(img1,128,255,cv2.THRESH_BINARY)
cv2.imshow("6",BINARY)
img1 = cv2.imread("lena.jpg",0)
_,BINARY = cv2.threshold(img1,128,255,cv2.THRESH_BINARY)
cv2.imshow("7",BINARY)



