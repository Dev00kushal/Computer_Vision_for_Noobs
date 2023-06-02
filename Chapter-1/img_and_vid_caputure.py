import cv2 as cv

#  We will be reading the image
img = cv.imread("Chapter-1/Resources/Lenna.png")
cv.imshow("Image_analysis",img)

# This is for the video 
frame_width = 600
frame_height = 600
cap = cv.VideoCapture("Chapter-1/Resources/dog_video.mp4") 
while True:
     sucess, image = cap.read()
     image = cv.resize(image,(frame_width,frame_height))
     cv.imshow("Video_analysis", image)

     if cv.waitKey(1) & 0XFF == ord("q"):
                break   

cv.release()
cv.destroyAllWindows()

