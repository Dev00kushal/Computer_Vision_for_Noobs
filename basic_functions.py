import cv2 as cv
path = "Resources/Lenna.png"
img =  cv.imread(path)
cv.imshow("Lenna_img",img)
cv.waitKey(0)