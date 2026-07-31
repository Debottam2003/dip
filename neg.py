import cv2
import numpy as np
i1 = cv2.imread("moon.jpg",0)
i2 = cv2.imread("lena.jpg",0)
i1 = cv2.resize(i1,(550,550))
i2 = cv2.resize(i2,(550,550))
i3 = np.add(i2,i1)
# neg_i = 255 - i
cv2.imshow("negative",i3)
cv2.waitKey(0)