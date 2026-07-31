import cv2
import numpy as np
img = cv2.imread("lena.jpg")

b,g,r = cv2.split(img)

zero = np.zeros_like(r)
bg = cv2.merge([b,g,zero]) # red removed
gr = cv2.merge([zero,g,r]) # blue removed
br = cv2.merge([b,zero,r]) # green removed

cv2.imshow("bg",bg)
cv2.imshow("gr",gr)
cv2.imshow("br",br)

