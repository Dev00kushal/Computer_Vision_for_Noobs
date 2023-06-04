import numpy as np
import cv2 as cv

circles = np.zeros((4, 2), dtype="float32")
image = cv.imread("Chapter-5/Resources/book.jpeg")
counter = 0

def Mouse_click(event, x, y, flags, parameter):
    global counter
    if event == cv.EVENT_FLAG_LBUTTON and counter < 4: 
        print(circles)
        circles[counter] = [x, y]
        counter += 1
        if counter == 4:
            width, height = 250, 350
            position1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
            position2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            matrix = cv.getPerspectiveTransform(position1, position2)
            image_output = cv.warpPerspective(image, matrix, (width, height))
            
            image_output = cv.convertScaleAbs(image_output, alpha=1.2, beta=10)  
            image_output = cv.GaussianBlur(image_output, (5, 5), 0)  
            image_output = cv.addWeighted(image_output, 1.5, image_output, -0.5, 0)  
            
            cv.imshow("Selected_image", image_output)

cv.imshow("Card_picture", image)
cv.setMouseCallback("Card_picture", Mouse_click)
cv.waitKey(0)
cv.destroyAllWindows()
