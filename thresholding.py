import cv2
import numpy as np
def thresh(i,thresh_value):
    _,threshold_i = cv2.threshold(i,thresh_value,255,cv2.THRESH_BINARY)
    return threshold_i
i = cv2.imread("lena.jpg",0)
thresh_value = int(input("Enter a thresh value:"))
if thresh_value >255 or thresh_value <0:
    print("Enter a threshold value again!")
else:
    threshold_i = thresh(i,thresh_value)
    cv2.imshow("threshold_image.jpg",threshold_i)
    cv2.waitKey(0)
