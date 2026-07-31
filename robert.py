import cv2
import numpy as np
img = cv2.imread("lena.jpg")
kernalx = np.array([[1,0],[0,-1]])
kernaly = np.array([[0,1],[-1,0]])
robx = cv2.filter2D(img,-1,kernalx)
roby = cv2.filter2D(img,-1,kernaly)
rob = cv2.add(robx,roby)
cv2.imshow("rob",rob)
cv2.waitKey(0)