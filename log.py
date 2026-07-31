#log Transform
import cv2
import numpy as np
img = cv2.imread("lena.jpg",0)
print(np.max(img))
img_log = np.log1p(img)
print(img_log)
c = 255 / np.max(img)
img_log = img_log * c
img_log = img_log.astype(np.uint8)
cv2.imwrite("log2.jpg",img_log)
print(img_log)
log = cv2.imread("log.jpg")
cv2.imshow("res",log)
cv2.waitKey(0)
cv2.destroyAllWindows()
