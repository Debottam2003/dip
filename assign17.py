import cv2
import numpy as np

def region_growing(image, seed, threshold):
    height, width = image.shape
    segmented = np.zeros_like(image, dtype=np.uint8)
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = [seed]
    seed_value = image[seed]
    while queue:
        current_pixel = queue.pop(0)
        if (
            0 <= current_pixel[0] < height
            and 0 <= current_pixel[1] < width
            and segmented[current_pixel] == 0
        ):
            diff = abs(int(image[current_pixel]) - int(seed_value))
            if diff <= threshold:
                segmented[current_pixel] = 255
                for neighbor in neighbors:
                    queue.append((current_pixel[0] + neighbor[0], current_pixel[1] + neighbor[1]))

    return segmented
seed_point = (50, 50)  
threshold_value = 20  
original_image = cv2.imread("OIP.jpg", cv2.IMREAD_GRAYSCALE)
segmented_image = region_growing(original_image, seed_point, threshold_value)
cv2.imwrite("Original Image.jpg", original_image)
cv2.imwrite("Segmented Image.jpg", segmented_image)
cv2.waitKey(0)