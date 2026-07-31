import cv2
import numpy as np
# i1 = cv2.imread("lena.jpg")
# i1=cv2.resize(i1,(1000,1000))
# #i1 = i1 * 0.5
# # cv2.imshow("i1",i1)
# # cv2.waitKey(0)
# i2 = cv2.imread("OIP.jpg")
# i2=cv2.resize(i2,(1000,1000))
# #i2 = i2 * 0.5
# #cv2.imshow("i2",i2)
# i_new = cv2.add(i1,i2)
# i_new = i_new * 1
# cv2.imshow("Result",i_new)
# cv2.waitKey(0)
img1 = cv2.imread('lena.jpg')
img2 = cv2.imread('moon.jpg')
img1 = cv2.resize(img1, (347, 403))
img2 = cv2.resize(img2, (347, 403))
img1 = img1 * 0.5
img2 = img2 * 0.5
avg_img = cv2.add(img1,img2)
cv2.imwrite('moon_lena.jpg',avg_img)
cv2.waitKey(0)