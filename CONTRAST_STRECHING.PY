import cv2
import numpy as np

# Load the image
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
print(image)

# Calculate minimum and maximum pixel values
min_val = np.min(image)
max_val = np.max(image)

# Define the desired minimum and maximum values for the output range (0-255 for 8-bit images)
out_min = 0
out_max = 255

# Perform contrast stretching
contrast_stretched = ((image - min_val) / (max_val - min_val)) * (out_max - out_min) + out_min

# Convert to uint8 data type
contrast_stretched = contrast_stretched.astype(np.uint8)
print(contrast_stretched)
# Display the original and contrast-stretched images
cv2.imshow('Original Image', image)
cv2.imwrite('Contrast_Stretched_Image.jpg', contrast_stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the contrast-stretched image
cv2.imwrite('contrast_stretched_image.jpg', contrast_stretched)
