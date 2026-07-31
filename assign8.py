import cv2
import numpy as np
i1=cv2.imread('lena.jpg')
i2=cv2.imread('download.jpg')
i1=cv2.resize(i1,(256,256))
i2=cv2.resize(i2,(256,256))
res=np.zeros(i1.shape,dtype=np.uint8)
for i in range(256):
    for j in range(128):
        res[i,j]=i1[i,j]
        res[i,j+128]=i2[i,j+128]
cv2.imshow('display.jpg',res)
cv2.waitKey(0)