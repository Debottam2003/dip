import numpy as np
import cv2

def main():
    print("Hello from dip!")
    img = cv2.imread("img2.png", cv2.IMREAD_COLOR)
    if img is None:
       print("Error: Could not read the image.")
       return
    else:
        print(img.shape)

    # Show image in a window
    cv2.imshow("Image Window", img)
    # Wait until a key is pressed
    cv2.waitKey(0)
    # Close the window
    cv2.destroyAllWindows()
    # cv2.imwrite("out.png")

if __name__ == "__main__":
    main()
