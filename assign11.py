import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('lena.jpg', 0)
brgt_enhan = cv2.convertScaleAbs(img, alpha=1.5, beta=70)
brgt_supp = cv2.convertScaleAbs(img, alpha=1.5, beta=-80)
contrast_change = cv2.convertScaleAbs(img, alpha=3, beta=0)
x, y = img.shape
grey_level_slicing = img.copy()
for i in range(0, x):
    for j in range(0, y):
        if img[i][j] > 100 and img[i][j] < 150:
           grey_level_slicing[i][j] = 255
        else:
            grey_level_slicing[i][j] = 0
figs, axs = plt.subplots(2, 2)
figs.suptitle('Image Enhancement')
axs[0, 0].imshow(grey_level_slicing, cmap='gray')
axs[0, 0].set_xticks([]), axs[0, 0].set_yticks([])
axs[0, 0].set_title('Grey Level Slicing w/o background')
axs[0, 1].imshow(brgt_supp, cmap='gray')
axs[0, 1].set_title('Brightness Suppressed')
axs[0, 1].set_xticks([]), axs[0, 1].set_yticks([])
axs[1, 0].imshow(brgt_enhan, cmap='gray')
axs[1, 0].set_title('Brightness Enhanced')
axs[1, 0].set_xticks([]), axs[1, 0].set_yticks([])
axs[1, 1].imshow(contrast_change, cmap='gray')
axs[1, 1].set_title('Contrast Manupulation')
axs[1, 1].set_xticks([]), axs[1, 1].set_yticks([])
figs.savefig('output_imgs/image_enhancement.png', bbox_inches='tight')