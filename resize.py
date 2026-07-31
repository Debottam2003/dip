import cv2
import numpy as np

img = cv2.imread("download.jpg",0)
cv2.imshow("Image",img)

cv2.imwrite('NEW.jpg',img)
