from tkinter import *
import cv2
import time
import cvzone
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import numpy as np

#gaame 1
from directkeys1 import PressKey, ReleaseKey
from directkeys1 import enter_pressed
#game 2
from directkeys2 import right_pressed, left_pressed
from directkeys2 import PressKey, ReleaseKey
#game 3
from directkeys3 import PressKey, ReleaseKey
from directkeys3 import space_pressed

root = Tk()
root.title("PLAYING WITH COMPUTER VISION ヾ(⌐■_■)ノ♪")

# Set the maximum pixel size
root.maxsize(850, 850)

def game1():
    print("Game 1 Selected")

    detector = HandDetector(detectionCon=0.5, maxHands=1)

    enter_key_pressed = enter_pressed

    time.sleep(2.0)

    current_key_pressed = set()

    video = cv2.VideoCapture(0)

    while True:
        ret, frame = video.read()
        keyPressed = False
        spacePressed = False
        key_count = 0
        key_pressed = 0
        hands, img = detector.findHands(frame)
        cv2.rectangle(img, (0, 480), (300, 425), (50, 50, 255), -2)
        cv2.rectangle(img, (640, 480), (400, 425), (50, 50, 255), -2)
        if hands:
            lmList = hands[0]
            fingerUp = detector.fingersUp(lmList)
            print(fingerUp)
            if fingerUp == [0, 0, 0, 0, 0]:
                cv2.putText(frame, 'Finger Count: 0', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, 'Jumping', (440, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
                PressKey(enter_key_pressed)
                spacePressed = True
                current_key_pressed.add(enter_key_pressed)
                key_pressed = enter_key_pressed
                keyPressed = True
                key_count = key_count + 1
            if fingerUp == [0, 1, 0, 0, 0]:
                cv2.putText(frame, 'Finger Count: 1', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
            if fingerUp == [0, 1, 1, 0, 0]:
                cv2.putText(frame, 'Finger Count: 2', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
            if fingerUp == [0, 1, 1, 1, 0]:
                cv2.putText(frame, 'Finger Count: 3', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
            if fingerUp == [0, 1, 1, 1, 1]:
                cv2.putText(frame, 'Finger Count: 4', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
            if fingerUp == [1, 1, 1, 1, 1]:
                cv2.putText(frame, 'Finger Count: 5', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
            if not keyPressed and len(current_key_pressed) != 0:
                for key in current_key_pressed:
                    ReleaseKey(key)
                current_key_pressed = set()
            elif key_count == 1 and len(current_key_pressed) == 2:
                for key in current_key_pressed:
                    if key_pressed != key:
                        ReleaseKey(key)
                current_key_pressed = set()
                for key in current_key_pressed:
                    ReleaseKey(key)
                current_key_pressed = set()
        cv2.imshow("Frame", frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    pass

def game2():
    print("Game 2 Selected")
    break_key_pressed = left_pressed
    accelerato_key_pressed = right_pressed

    time.sleep(2.0)
    current_key_pressed = set()

    mp_draw = mp.solutions.drawing_utils
    mp_hand = mp.solutions.hands

    tipIds = [4, 8, 12, 16, 20]

    video = cv2.VideoCapture(0)

    with mp_hand.Hands(min_detection_confidence=0.5,
                       min_tracking_confidence=0.5) as hands:
        while True:
            keyPressed = False
            break_pressed = False
            accelerator_pressed = False
            key_count = 0
            key_pressed = 0
            ret, image = video.read()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            lmList = []
            if results.multi_hand_landmarks:
                for hand_landmark in results.multi_hand_landmarks:
                    myHands = results.multi_hand_landmarks[0]
                    for id, lm in enumerate(myHands.landmark):
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])
                    mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
            fingers = []
            if len(lmList) != 0:
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1, 5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                total = fingers.count(1)
                if total == 0:
                    cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                    cv2.putText(image, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                                2, (255, 0, 0), 5)
                    PressKey(break_key_pressed)
                    break_pressed = True
                    current_key_pressed.add(break_key_pressed)
                    key_pressed = break_key_pressed
                    keyPressed = True
                    key_count = key_count + 1
                elif total == 5:
                    cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                    cv2.putText(image, " GAS", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                                2, (255, 0, 0), 5)
                    PressKey(accelerato_key_pressed)
                    key_pressed = accelerato_key_pressed
                    accelerator_pressed = True
                    keyPressed = True
                    current_key_pressed.add(accelerato_key_pressed)
                    key_count = key_count + 1
            if not keyPressed and len(current_key_pressed) != 0:
                for key in current_key_pressed:
                    ReleaseKey(key)
                current_key_pressed = set()
            elif key_count == 1 and len(current_key_pressed) == 2:
                for key in current_key_pressed:
                    if key_pressed != key:
                        ReleaseKey(key)
                current_key_pressed = set()
                for key in current_key_pressed:
                    ReleaseKey(key)
                current_key_pressed = set()

                # if lmList[8][2] < lmList[6][2]:
                #     print("Open")
                # else:
                #     print("Close")
            cv2.imshow("Frame", image)
            k = cv2.waitKey(1)
            if k == ord('q'):
                break
    video.release()
    cv2.destroyAllWindows()
    pass

def game3():
    print("Game 3 Selected")

    detector = HandDetector(detectionCon=0.8, maxHands=1)

    space_key_pressed = space_pressed

    time.sleep(2.0)

    current_key_pressed = set()

    video = cv2.VideoCapture(0)

    while True:
        ret, frame = video.read()
        keyPressed = False
        spacePressed = False
        key_count = 0
        key_pressed = 0
        hands, img = detector.findHands(frame)
        cv2.rectangle(img, (0, 480), (300, 425), (50, 50, 255), -2)
        cv2.rectangle(img, (640, 480), (400, 425), (50, 50, 255), -2)
        if hands:
            lmList = hands[0]

            fingerUp = detector.fingersUp(lmList)
            print(fingerUp)
            if fingerUp == [0, 0, 0, 0, 0]:
                cv2.putText(frame, 'Finger Count: 0', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, 'Jumping', (440, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
                PressKey(space_key_pressed)
                spacePressed = True
                current_key_pressed.add(space_key_pressed)
                key_pressed = space_key_pressed
                keyPressed = True
                key_count = key_count + 1
            if fingerUp == [0, 1, 0, 0, 0]:
                cv2.putText(frame, 'Finger Count: 1', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
            if fingerUp == [0, 1, 1, 0, 0]:
                cv2.putText(frame, 'Finger Count: 2', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
            if fingerUp == [0, 1, 1, 1, 0]:
                cv2.putText(frame, 'Finger Count: 3', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
            if fingerUp == [0, 1, 1, 1, 1]:
                cv2.putText(frame, 'Finger Count: 4', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
            if fingerUp == [1, 1, 1, 1, 1]:
                cv2.putText(frame, 'Finger Count: 5', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, 'Not Jumping', (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
            if not keyPressed and len(current_key_pressed) != 0:
                for key in current_key_pressed:
                    ReleaseKey(key)
                current_key_pressed = set()
            elif key_count == 1 and len(current_key_pressed) == 2:
                for key in current_key_pressed:
                    if key_pressed != key:
                        ReleaseKey(key)
                current_key_pressed = set()
                for key in current_key_pressed:
                    ReleaseKey(key)
                current_key_pressed = set()
        cv2.imshow("Frame", frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    pass

def game4():

    print("Game 4 Selected")
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    # Importing all images
    imgBackground = cv2.imread("Resources/Background.png")
    imgGameOver = cv2.imread("Resources/gameOver.png")
    imgBall = cv2.imread("Resources/Ball.png", cv2.IMREAD_UNCHANGED)
    imgBat1 = cv2.imread("Resources/bat1.png", cv2.IMREAD_UNCHANGED)
    imgBat2 = cv2.imread("Resources/bat2.png", cv2.IMREAD_UNCHANGED)

    # Hand Detector
    detector = HandDetector(detectionCon=0.8, maxHands=2)

    # Variables
    ballPos = [100, 100]
    speedX = 15
    speedY = 15
    gameOver = False
    score = [0, 0]

    while True:
        _, img = cap.read()
        img = cv2.flip(img, 1)
        imgRaw = img.copy()

        # Find the hand and its landmarks
        hands, img = detector.findHands(img, flipType=False)  # with draw

        # Overlaying the background image
        img = cv2.addWeighted(img, 0.2, imgBackground, 0.8, 0)

        # Check for hands
        if hands:
            for hand in hands:
                x, y, w, h = hand['bbox']
                h1, w1, _ = imgBat1.shape
                y1 = y - h1 // 2
                y1 = np.clip(y1, 20, 415)

                if hand['type'] == "Left":
                    img = cvzone.overlayPNG(img, imgBat1, (59, y1))
                    if 59 < ballPos[0] < 59 + w1 and y1 < ballPos[1] < y1 + h1:
                        speedX = -speedX
                        ballPos[0] += 30
                        score[0] += 1

                if hand['type'] == "Right":
                    img = cvzone.overlayPNG(img, imgBat2, (1195, y1))
                    if 1195 - 50 < ballPos[0] < 1195 and y1 < ballPos[1] < y1 + h1:
                        speedX = -speedX
                        ballPos[0] -= 30
                        score[1] += 1

        # Game Over
        if ballPos[0] < 40 or ballPos[0] > 1200:
            gameOver = True

        if gameOver:
            img = imgGameOver
            cv2.putText(img, str(score[1] + score[0]).zfill(2), (585, 360), cv2.FONT_HERSHEY_COMPLEX,
                        2.5, (200, 0, 200), 5)

        # If game not over move the ball
        else:

            # Move the Ball
            if ballPos[1] >= 500 or ballPos[1] <= 10:
                speedY = -speedY

            ballPos[0] += speedX
            ballPos[1] += speedY

            # Draw the ball
            img = cvzone.overlayPNG(img, imgBall, ballPos)

            cv2.putText(img, str(score[0]), (300, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
            cv2.putText(img, str(score[1]), (900, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)

        img[580:700, 20:233] = cv2.resize(imgRaw, (213, 120))

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)
        if key == ord('r'):
            ballPos = [100, 100]
            speedX = 15
            speedY = 15
            gameOver = False
            score = [0, 0]
            imgGameOver = cv2.imread("Resources/gameOver.png")
        if key == ord('q'):
            break
    pass


# create photo image objects from image files
img1 = PhotoImage(file="game1.png")
img2 = PhotoImage(file="game2.png")
img3 = PhotoImage(file="game3.png")
img4 = PhotoImage(file="game4.png")

# create buttons with the photo images
btn1 = Button(root, image=img1, command=game1, borderwidth=10)
btn2 = Button(root, image=img2, command=game2, borderwidth=10)
btn3 = Button(root, image=img3, command=game3, borderwidth=10)
btn4 = Button(root, image=img4, command=game4, borderwidth=10)

# pack the buttons into the window
btn1.grid(row=0, column=0, pady=10, padx=20)
btn2.grid(row=0, column=1, pady=10, padx=20)
btn3.grid(row=1, column=0, pady=10, padx=20)
btn4.grid(row=1, column=1, pady=10, padx=20)

root.mainloop()
