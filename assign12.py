import cv2
import numpy as np
def apply_mean_filter(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))
def apply_weighted_average_filter(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    return cv2.filter2D(image, -1, kernel)
def apply_median_filter(image, kernel_size):
    return cv2.medianBlur(image, kernel_size)
def apply_max_min_filter(image, kernel_size):
    max_filtered = cv2.dilate(image, np.ones((kernel_size, kernel_size), np.uint8))
    min_filtered = cv2.erode(image, np.ones((kernel_size, kernel_size), np.uint8))
    return max_filtered - min_filtered
def main():
    original_image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
    kernel_size = int(input("Enter kernel size (odd integer): "))
    if kernel_size % 2 == 0:
        print("Please enter an odd integer for the kernel size.")
        return
    mean_filtered = apply_mean_filter(original_image, kernel_size)
    weighted_average_filtered = apply_weighted_average_filter(original_image, kernel_size)
    median_filtered = apply_median_filter(original_image, kernel_size)
    max_min_filtered = apply_max_min_filter(original_image, kernel_size)
    cv2.imshow('Original Image', original_image)
    cv2.imwrite('Mean Filtered.jpg', mean_filtered)
    cv2.imwrite('Weighted Average Filtered.jpg', weighted_average_filtered)
    cv2.imwrite('Median Filtered.jpg', median_filtered)
    cv2.imwrite('Max-Min Filtered.jpg', max_min_filtered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()