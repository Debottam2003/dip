import cv2
import numpy as np
def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = image.copy()
    salt_mask = np.random.random(image.shape) < salt_prob
    noisy_image[salt_mask] = 255
    pepper_mask = np.random.random(image.shape) < pepper_prob
    noisy_image[pepper_mask] = 0
    return noisy_image

original_image = cv2.imread('lena.jpg',0)
salt_probability = float(input("Enter probability for salt noise (0 to 1): "))
pepper_probability = float(input("Enter probability for pepper noise (0 to 1): "))
noisy_image = add_salt_and_pepper_noise(original_image, salt_probability, pepper_probability)
cv2.imshow('Original Image', original_image)
cv2.imshow('Noisy Image.jpg0', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
