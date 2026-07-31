import cv2
import numpy as np
img = cv2.imread("lena.jpg",0)
for i in img:
    print(i)