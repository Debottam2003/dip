import cv2
import numpy as np
img1 = cv2.imread("lena.jpg")
img2 = img1.copy()
#print(img2)
#cv2.imshow("output",img1)
#b,g,r = cv2.split(img1)
#zero = np.zeros_like(r)
#b_c=cv2.merge([b,zero,zero])
#g_c=cv2.merge([zero,g,zero])
#r_c=cv2.merge([zero,zero,r])
#cv2.imshow("blue",b_c)
#print(b_c)
#cv2.imshow("green",g_c)
#print(g_c)
#cv2.imshow("red",r_c)
#print(r_c)
#print(b)
#print(g)
#print(r)
img1[:,:,0]=0
img1[:,:,1]=0
cv2.imshow("red",img1)
print(img1)
img1=img2.copy()
img1[:,:,0]=0
img1[:,:,2]=0
cv2.imshow("green",img1)
print(img1)
img1=img2.copy()
img1[:,:,2]=0
img1[:,:,1]=0
cv2.imshow("blue",img1)
print(img1)


