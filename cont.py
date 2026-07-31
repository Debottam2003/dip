import cv2
import numpy as np
i = cv2.imread("lena.jpg")
cv2.imshow("input",i)
print("input\n",i)
imax = 255
imin = 0

rmax = np.max(i)
rmin = np.min(i)

con = ((i - rmin) / (rmax - rmin)) * (imax - imin) + imin
con = con.astype(np.uint8)
cv2.imshow("output",con)
print("output\n",con)
cv2.waitKey(0)