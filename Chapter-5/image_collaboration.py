import cv2 as cv
import numpy as np
path = "Chapter-2/Resources/Lenna.png"
kernel = np.ones((5,5),np.uint8)
img = cv.imread(path)
def Gray__image():
    gray_image = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("Gray_lenna_image",gray_image)
    
def Blur__image():
    blur_image = cv.GaussianBlur(img,(5,5),0)
    cv.imshow("Blur_Lenna_image",blur_image)
    
def Canny__image():
    canny_image = cv.Canny(img,100,100)
    cv.imshow("Canny_Lenna_image",canny_image)

def dilated__image():
    dilated_image = cv.dilate(img,kernel,iterations=1)
    cv.imshow("Dilated_image",dilated_image)

def eroded__image():
    eroded_image = cv.erode(img,kernel,iterations=2)
    cv.imshow("Eroded_image",eroded_image)

Canny__image()
Blur__image()
Gray__image()
dilated__image()
eroded__image()
cv.waitKey(0)