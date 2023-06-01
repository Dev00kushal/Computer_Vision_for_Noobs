import cv2 as cv    
path = "Chapter-3/Resources/rose.jpeg"
img = cv.imread(path)

def Resized_image():
    width,height = 800,500
    img_resize = cv.resize(img,(width,height))
    print(img_resize.shape)
    cv.imshow("Resized_Lenna_img_",img_resize)

def Cropped_image():
    img_cropped = img[0:600,100:500]  # img[h,w]
    cv.imshow("Cropped_image",img_cropped)

Resized_image()
Cropped_image()
cv.waitKey(0)