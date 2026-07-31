import cv2
import numpy as np
def image_negative(image):
    return 255 - image
def log_transformation(image, c=8):
    return c * np.log1p(image)
def power_law_transformation(image, gamma=1):
    return np.power(image, gamma)
def piecewise_linear_transform(image, points):
    lut = np.zeros(256, dtype=np.uint8)
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        slope = (y1 - y0) / (x1 - x0)
        intercept = y0 - slope * x0
        lut[x0:x1] = np.clip(np.round(np.arange(x0, x1) * slope + intercept), 0, 255)
    return cv2.LUT(image, lut)
if __name__ == "__main__":
    # Replace 'your_image.jpg' with the actual filename of the image
    image_path = 'lena.jpg'
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    negative_image = image_negative(original_image)
    log_transformed_image = log_transformation(original_image)
    power_law_transformed_image = power_law_transformation(original_image, gamma=0.9)
    points = [(0, 50), (100, 150), (200, 100), (255, 255)]
    piecewise_linear_transformed_image = piecewise_linear_transform(original_image, points)
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Image Negative', negative_image)
    cv2.imshow('Log Transformation', log_transformed_image.astype(np.uint8))
    cv2.imshow('Power-law Transformation', power_law_transformed_image.astype(np.uint8))
    cv2.imshow('Piecewise Linear Transformation', piecewise_linear_transformed_image)
    cv2.waitKey(0)
    