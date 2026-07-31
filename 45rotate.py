import cv2
import numpy as np
i = cv2.imread("lena.jpg")
h,w = i.shape[:2]
angle = 45
clk = cv2.getRotationMatrix2D((w/2,h/2),-angle,1)
anticlk = cv2.getRotationMatrix2D((w/2,h/2),angle,1)
clk_i = cv2.warpAffine(i,clk,(w,h))
anticlk_i = cv2.warpAffine(i,anticlk,(w,h))
cv2.imshow("clock",clk_i)
cv2.imshow("Anticlock",anticlk_i)
cv2.waitKey(0)