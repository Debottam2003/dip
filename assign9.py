import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
binary_image = np.unpackbits(image, axis=-1)
bit_planes = [np.bitwise_and(binary_image, 2**i) for i in range(7, -1, -1)]
for i, plane in enumerate(bit_planes):
    plt.subplot(3, 3, i+1)
    plt.imshow(plane * 255, cmap='gray')
    plt.title(f'Bit Plane {i}')
    plt.axis('off')
plt.show()