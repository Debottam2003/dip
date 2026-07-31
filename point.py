import cv2
import numpy as np
i = cv2.imread("lena.jpg")
p = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
j = cv2.filter2D(i,-1,p)
cv2.imshow("point",j)
cv2.waitKey(0)