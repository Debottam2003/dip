import cv2
import numpy as np
def salt_pepper(i,salt_p,pepper_p):
    ni = i.copy()
    salt_mask = np.random.random(i.shape) < salt_p
    ni[salt_mask] = 255
    pepper_mask = np.random.random(i.shape) < pepper_p
    ni[pepper_mask] = 0
    return ni
i = cv2.imread("lena.jpg",0)
salt_p = float(input("Enter salt noise probability(0 to 1):"))
pepper_p = float(input("Enter pepper noise probability(0 to 1):"))
ni = salt_pepper(i,salt_p,pepper_p)
cv2.imshow("input_image",i)
cv2.imshow("salt_pepper_noise_image",ni)
cv2.imwrite("salt_pepper_noise_image.jpg",ni)
cv2.waitKey(0)


