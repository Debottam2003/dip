import cv2
import numpy as np
i = cv2.imread("lena.jpg")
j = cv2.imread("download.jpg")
i = cv2.resize(i,(250,250))
j = cv2.resize(j,(250,250))
print(i)
i = (i * 0.5).astype(np.uint8)
print(i)
j = (j * 0.5).astype(np.uint8)
k = cv2.add(i,j)
cv2.imshow("res",k)
cv2.waitKey(0) 