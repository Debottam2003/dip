import cv2
import numpy as np
img = cv2.imread("download.jpg")
cv2.imshow("Okusera",img)
cv2.waitKey(0)
img2 = img[:,:,0]
cv2.imshow("Okusera",img2)
cv2.waitKey(0)
img3 = img[:,:,1]
cv2.imshow("Okusera",img3)
cv2.waitKey(0)
img4 = img[:,:,2]
cv2.imshow("Okusera",img4)
cv2.waitKey(0)

img[:,:,0]=0
cv2.imshow("Okusera",img)
cv2.waitKey(0)
img[:,:,1]=0
cv2.imshow("Okusera",img)
cv2.waitKey(0)
img[:,:,2]=0
cv2.imshow("Okusera",img)
cv2.waitKey(0)

img_new = np.hstack((img2,img3,img4))
cv2.imshow("tupple",img_new)
