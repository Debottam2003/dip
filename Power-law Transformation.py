import cv2
import numpy as np
img = cv2.imread("lena.jpg",0)
gama = 0.5
norm_img = img / 255
pow_img = np.power(norm_img,gama)
pow_img = (pow_img * 255).astype(np.uint8)
img2 = pow_img.copy()
cv2.imshow("log",img2)
cv2.waitKey(0)
# import cv2
# import numpy as np
img1 = cv2.imread("lena.jpg",0)
gamma = 0.9
img1 = img1 / 255
power = np.power(img1,gamma)
power = (power * 255).astype(np.uint8)
print(power)
cv2.imshow("output",power)
cv2.waitKey(0)