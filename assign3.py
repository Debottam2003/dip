# import cv2
# import numpy as np
# original_image = cv2.imread("lena.jpg")
# clockwise_rotated_image = cv2.rotate(original_image, cv2.ROTATE_90_CLOCKWISE)
# anticlockwise_rotated_image = cv2.rotate(original_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.imshow('Original Image', original_image)
# cv2.imshow('Clockwise Rotated Image', clockwise_rotated_image)
# cv2.imshow('Anticlockwise Rotated Image', anticlockwise_rotated_image)
# cv2.waitKey(0)
import cv2

# Read the input image
input_image = cv2.imread('lena.jpg')

# Get image dimensions
height, width = input_image.shape[:2]

# Define the angle of rotation (in degrees)
angle = 60

# Define the rotation matrix for clockwise rotation
rotation_matrix_clockwise = cv2.getRotationMatrix2D((width/2, height/2), -angle, 1)

# Define the rotation matrix for anti-clockwise rotation
rotation_matrix_anticlockwise = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)

# Apply rotation
rotated_image_clockwise = cv2.warpAffine(input_image, rotation_matrix_clockwise, (width, height))
rotated_image_anticlockwise = cv2.warpAffine(input_image, rotation_matrix_anticlockwise, (width, height))

# Display the original and rotated images
cv2.imshow('Original Image', input_image)
cv2.imshow('Clockwise Rotation (45°)', rotated_image_clockwise)
cv2.imshow('Anti-clockwise Rotation (45°)', rotated_image_anticlockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()