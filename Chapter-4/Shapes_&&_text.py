import numpy as np
import cv2 as cv

path = "Chapter-4/Resources/Huskey.jpg"

img = cv.imread(path)


def Regular_image():
    cv.imshow("Huskey_img", img)

def Blank_image():
    blank_image = np.zeros((500,1000),np.uint8)
    cv.imshow("Blank_image",blank_image)


def Colored_image():
    refuge_image = np.zeros((500,500,3),np.uint8)
    print(refuge_image)



Regular_image()
Colored_image()
Blank_image()
cv.waitKey(0)
