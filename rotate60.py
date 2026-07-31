# Read the input image
import cv2
import numpy as np
input_image = cv2.imread('lena.jpg')
h,w = input_image.shape[:2]
angle = 45
clock = cv2.getRotationMatrix2D((w/2,h/2),-angle,1)
anticlock = cv2.getRotationMatrix2D((w/2,h/2),angle,1)
clock_img = cv2.warpAffine(input_image,clock,(w,h))
anticlock_img = cv2.warpAffine(input_image,anticlock,(w,h))
# Get image dimensions
# height, width = input_image.shape[:2]
# # Define the angle of rotation (in degrees)
# angle = 60
# # Define the rotation matrix for clockwise rotation
# rotation_matrix_clockwise = cv2.getRotationMatrix2D((width/2, height/2), -angle, 1)
# # Define the rotation matrix for anti-clockwise rotation
# rotation_matrix_anticlockwise = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
# # Apply rotation
# rotated_image_clockwise = cv2.warpAffine(input_image, rotation_matrix_clockwise, (width, height))
# rotated_image_anticlockwise = cv2.warpAffine(input_image, rotation_matrix_anticlockwise, (width, height))
# # Display the original and rotated images
cv2.imshow('Original Image', input_image)
cv2.imshow('Clockwise Rotation (45°)', clock_img)
cv2.imshow('Anti-clockwise Rotation (45°)', anticlock_img)
cv2.waitKey(0)
cv2.destroyAllWindows()