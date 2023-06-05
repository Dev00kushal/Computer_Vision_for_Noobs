import cv2
from cvzone.HandTrackingModule import HandDetector
import math

class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (250, 251, 217), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 40),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

    def checkClicking(self, x, y):
        cx = self.pos[0] + self.width // 2  # x-coordinate of button center
        cy = self.pos[1] + self.height // 2  # y-coordinate of button center
        dist = math.hypot(x - cx, y - cy)  # distance between the point and button center
        if dist < self.width // 2:
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (255, 255, 255), cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (50, 50, 50), 3)
            cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 50),
                        cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 4)
            return True
        else:
            return False

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

buttonListValue = [["1", "2", "3", "+"],
                   ["4", "5", "6", "-"],
                   ["7", "8", "9", "*"],
                   ["0", "/", ".", "="]]
buttonList = []
for x in range(4):
    for y in range(4):
        xPos = x * 70 + 350
        yPos = y * 70 + 100
        buttonList.append(Button((xPos, yPos), 70, 70, buttonListValue[x][y]))

equation = ""
delayCounter = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, flipType=False)

    cv2.rectangle(img, (350, 30), (350 + 280, 100), (250, 251, 217), cv2.FILLED)
    cv2.rectangle(img, (350, 30), (350 + 280, 100), (50, 50, 50), 3)

    for button in buttonList:
        button.draw(img)

    if hands and len(hands) > 0:
        hand = hands[0]
        lmList = hand["lmList"]
        if len(lmList) >= 13:
            x1, y1, _ = lmList[8]
            x2, y2, _ = lmList[12]

            for button in buttonList:
                if button.checkClicking(x1, y1) and delayCounter == 0:
                    if button.value == "=":
                        equation = str(eval(equation))
                    else:
                        equation += button.value
                    delayCounter = 1

    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0

    cv2.putText(img, equation, (355, 80), cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)
    cv2.imshow("Virtual_Calculator", img)
    key = cv2.waitKey(1)
    if key == ord("c"):
        equation = ""
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()