import cv2
import numpy as np
img = cv2.imread("lena.jpg",0)
cv2.imshow("input",img)

imax = 255
imin = 0

rmax = np.max(img)
rmin = np.min(img)

contrast = ((img - rmin) / (rmax - rmin) ) * (imax - imin) + imin
contrast = contrast.astype(np.uint8)

cv2.imshow("output",contrast)


