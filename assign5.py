import cv2
import numpy as np
def color_separation(image):
    b, g, r = cv2.split(image)
    zeros = np.zeros_like(b)
    blue_channel = cv2.merge([b, zeros, zeros])
    green_channel = cv2.merge([zeros, g, zeros])
    red_channel = cv2.merge([zeros, zeros, r])
    return red_channel, green_channel, blue_channel
if __name__ == "__main__":
    # Replace 'your_image.jpg' with the actual filename of the color image
    image_path = 'lena.jpg'
    color_image = cv2.imread(image_path)
    red_channel, green_channel, blue_channel = color_separation(color_image)
    #cv2.imshow('Original Image', color_image)
    cv2.imwrite('Red Channel.jpg', red_channel)
    cv2.imwrite('Green Channel.jpg', green_channel)
    cv2.imwrite('Blue Channel.jpg', blue_channel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# import cv2
# import numpy as np
# i = cv2.imread("lena.jpg")
# img = i.copy()
# IMG_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# img[:,:,0]=0
# img[:,:,1]=0
# cv2.imshow("red",img)
# cv2.waitKey(0)
# img = i.copy()
# img[:,:,0]=0
# img[:,:,2]=0
# cv2.imshow("green",img)
# cv2.waitKey(0)
# img = i.copy()
# img[:,:,2]=0
# img[:,:,1]=0
# cv2.imshow("blue",img)
# cv2.waitKey(0)
