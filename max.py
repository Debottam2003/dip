import cv2
import numpy as np
img = cv2.imread("lena.jpg")
print(np.max(img))
img_log = np.log1p(img)
img_log = (img_log * 255 )/np.max(img_log)
cv2.imwrite("log2.jpg",img_log)
log = cv2.imread("log.jpg")
cv2.imshow("res",log)
cv2.waitKey(0)
cv2.destroyAllWindows()