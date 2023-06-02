import numpy as np
import cv2 as cv
def Blank_image():
    blank_image = np.zeros((500,500),np.uint8)
    cv.imshow("Blank_image",blank_image)

def Colored_image():
    reused_image = np.zeros((500,500,3),np.uint8)
    reused_image[:] = 0,200,4
    cv.imshow("Colored_image",reused_image)

def lined_image():
    reused_image = np.zeros((500, 500, 3), np.uint8)
    cv.line(reused_image, (100, 100), (200, 0), (255, 100, 200), 3)
    cv.imshow("Lined_image", reused_image)

def rectangled_image():
    reused_image = np.zeros((500, 500, 3), np.uint8)
    cv.rectangle(reused_image,(300,300),(50,50),(0,255,0),2)
    cv.imshow("Rectnagle_image",reused_image)

def circled_image():
    reused_image = np.zeros((500, 500, 3), np.uint8)
    cv.circle(reused_image,(200,200),(100),(255,200,100),2)
    cv.imshow("Circled_image",reused_image)


def texted_image():
     reused_image = np.zeros((500, 500, 3), np.uint8)
     cv.addText(reused_image,"This is a written text",(20,20),"Ubuntu",10,(255,200,200),10)
     cv.imshow("Texted_image",reused_image)


rectangled_image()
Colored_image()
lined_image()
Blank_image()
texted_image()
circled_image()
cv.waitKey(0)
cv.destroyAllWindows()
