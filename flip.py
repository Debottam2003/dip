import cv2
import numpy as np
img = cv2.imread("download.jpg")

img_flip1=cv2.flip(img,1)
img_flip2=cv2.flip(img,0)
img_flip3=cv2.flip(img,-1)

img_new = np.hstack((img,img_flip1,img_flip2,img_flip3))
cv2.imshow("flip",img_new)
cv2.waitKey(0)
