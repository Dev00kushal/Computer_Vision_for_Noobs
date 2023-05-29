import cv2 as cv

# 1. Image_Read
img = cv.imread("Images/Lenna.png")
cv.imshow("Lenna_img_detection",img)
cv.waitKey(0)
    