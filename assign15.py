import cv2
import numpy as np
def global_thresholding(image, threshold_value):
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image
def main():
    original_image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Original Image', original_image)
    threshold_value = int(input("Enter the threshold value (0 to 255): "))
    if not (0 <= threshold_value <= 255):
        print("Please enter a valid threshold value between 0 and 255.")
        return
    binary_image = global_thresholding(original_image, threshold_value)
    cv2.imwrite('Binary Image.jpg', binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
