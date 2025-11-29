# import cv2

# img = cv2.imread('cloudflare.png', cv2.IMREAD_GRAYSCALE)

# img[:] = 255 - img
# # Invert the grayscale image(White to Black and Black to White)

# cv2.imshow('Grayscale Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imwrite('inverted_cloudflare.png', img)

import cv2

img = cv2.imread('cloudflare.png', cv2.IMREAD_GRAYSCALE)

img[:] = img + 50
# Invert the grayscale image(White to Black and Black to White)

cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite('inverted_cloudflare.png', img)