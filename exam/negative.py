import numpy as np

img = np.array([
    [45,120,200,30],
    [60,90,150,210],
    [15,180,75,135],
    [255,0,100,170]
    ])

def negative(image):
    for i in range(len(image)):
        for j in range(len(image[0])):
            image[i][j] = 255 - image[i][j]
    print(image)

negative(img)