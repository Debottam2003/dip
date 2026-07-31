import cv2
import matplotlib.pyplot as plt

# Read the input image in grayscale
image = cv2.imread('contrast_streched_image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("input",image)
# Calculate histogram using OpenCV
histogram = cv2.calcHist([image], [0], None,[256], [0,256])

# Plot the histogram
plt.figure()
plt.title('Histogram of the Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.plot(histogram)
plt.show()
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
i = cv2.equalizeHist(image)
# Calculate histogram using OpenCV
histogram = cv2.calcHist([i], [0], None,[256], [0,256])
cv2.imshow("out",i)
# Plot the histogram
plt.figure()
plt.title('Histogram of the Image')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.plot(histogram)
plt.show()