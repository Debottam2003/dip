import cv2
import numpy as np
def local_thresholding(image, thresholds):
    rows, cols = image.shape[:2]
    mid_row, mid_col = rows // 2, cols // 2
    binary_image = np.zeros_like(image, dtype=np.uint8)
    binary_image[:mid_row, :mid_col] = cv2.threshold(image[:mid_row, :mid_col], thresholds[0], 255, cv2.THRESH_BINARY)[1]
    binary_image[:mid_row, mid_col:] = cv2.threshold(image[:mid_row, mid_col:], thresholds[1], 255, cv2.THRESH_BINARY)[1]
    binary_image[mid_row:, :mid_col] = cv2.threshold(image[mid_row:, :mid_col], thresholds[2], 255, cv2.THRESH_BINARY)[1]
    binary_image[mid_row:, mid_col:] = cv2.threshold(image[mid_row:, mid_col:], thresholds[3], 255, cv2.THRESH_BINARY)[1]
    return binary_image
def main():
    original_image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Original Image', original_image)
    thresholds = []
    for i in range(4):
        threshold_value = int(input(f"Enter the threshold value for quadrant {i + 1} (0 to 255): "))
        thresholds.append(threshold_value)
    if any(not (0 <= threshold <= 255) for threshold in thresholds):
        print("Please enter valid threshold values between 0 and 255.")
        return
    binary_image = local_thresholding(original_image, thresholds)
    cv2.imwrite('Binary Image2.jpg', binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()