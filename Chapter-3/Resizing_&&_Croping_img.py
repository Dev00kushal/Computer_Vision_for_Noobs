import cv2 as cv    
path = "Chapter-3/Resources/rose.jpeg"
img = cv.imread(path)

def Resized_image():
    width,height = 400,400
    img_resize = cv.resize(img,(width,height))
    print(img_resize.shape)
    cv.imshow("Resized_Lenna_img_",img_resize)

Resized_image()
cv.waitKey(0)