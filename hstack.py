import cv2
import numpy as np
img = cv2.imread("download.jpg")
img1 = img[:,:,0]
img2 = img[:,:,1]
img3 = img[:,:,2]
img_new = np.hstack((img1,img2,img3))
cv2.imshow("tupple",img_new)
print(img.shape)
img_resize = cv2.resize(img,(550,450))
cv2.imshow("size",img_resize)
img_resize2 = cv2.resize(img,(img.shape[1]*2,img.shape[0]*2))
cv2.imshow("size",img_resize2)
cv2.waitKey(0)

