import cv2
import numpy as np
def negative(img):
    neg_img = 255 - img
    return(neg_img)  
img = cv2.imread("lena.jpg",0)
c=8
gama = 0.5
norm_img = img / 255
pow_img = np.power(norm_img,gama)
pow_img = (pow_img * 255).astype(np.uint8)
#img1 = negative(img)
#cv2.imshow("negative",img1)
img2 = pow_img.copy()
cv2.imshow("log",img2)
cv2.waitKey(0)




