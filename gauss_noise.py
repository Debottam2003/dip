import cv2
import numpy as np
# Read the input image
image = cv2.imread('lena.jpg',0)
# Generate Gaussian noise with the same shape as the image
gaussian_noise = np.random.normal(25, 125, image.shape).astype(np.uint8)
# Add Gaussian noise to the image
noisy_image = cv2.add(image, gaussian_noise)
# Display the original and noisy images
cv2.imshow('Original Image', image)
cv2.imshow('Noisy Image', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()