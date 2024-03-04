import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui as auto

# Function to draw a button
def draw_button(img, text, pos, size=(120, 60), color=(200, 200, 200)):
    x, y = pos
    w, h = size
    cv2.rectangle(img, (x, y), (x + w, y + h), color, cv2.FILLED)
    cv2.putText(img, text, (x + 10, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cap = cv2.VideoCapture(0)
hd = HandDetector(maxHands=1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Resize the frame while maintaining the aspect ratio
    width = 720
    height = int((frame.shape[0] / frame.shape[1]) * width)
    frame = cv2.resize(frame, (width, height))

    # Add background
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    # Detect hand and get hand landmarks
    hand, frame = hd.findHands(frame)

    if hand:
        fingers = hd.fingersUp(hand[0])
        
        # Perform action based on hand gesture (e.g., start or jump)
        if fingers == [1, 1, 1, 1, 1]:  # All fingers raised
            auto.press('up')  # Press spacebar to jump
    cv2.imshow('Game', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
