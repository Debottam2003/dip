import cv2
import numpy as np
i1 = cv2.imread("OIP.jpg")
i2 = cv2.imread("lena.jpg")
i1=cv2.resize(i1,(500,500))
i2=cv2.resize(i2,(500,500))
i3 = cv2.subtract(i1,i2)
cv2.imwrite("sub.jpg",i3)
cv2.waitKey(0)
