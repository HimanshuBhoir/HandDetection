import cv2
import time
import os
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)

fldrPath = "Fingers"
myList = os.listdir(fldrPath)
print(myList)
# overlayList = []
# for imPath in myList:
    # image = cv2.imread(f'{fldrPath}/{imPath}')
    # print(f'{fldrPath}/{imPath}')
    # overlayList.append(image)

# print(len(overlayList))

pTime = 0

detector = htm.handDetector(detectionCon=0.7)

tipIDs = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0 :
        finger = []
        # thumb
        if lmList[tipIDs[0]][1] > lmList[tipIDs[0] - 1][1]:
            finger.append(1)
        else:
            finger.append(0)

        for id in range(1, 5):
            if lmList[tipIDs[id]][2] < lmList[tipIDs[id]-2][2] :
                finger.append(1)
            else:
                finger.append(0)
        # print(finger)
        totalFingers = finger.count(1)
        print(totalFingers)
        if totalFingers == 1:
            cv2.putText(img, f'Okay', (40, 400), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 4)
        elif totalFingers == 2:
            cv2.putText(img, f'Victory', (40, 400), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 4)
        elif totalFingers == 3 or totalFingers == 4:
            cv2.putText(img, f'Nice', (40, 400), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 4)
        elif totalFingers == 5:
            cv2.putText(img, f'Stop', (40, 400), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 4)
        # h, w, c = overlayList[totalFingers].shape
        # img[0:h, 0:w] = overlayList[totalFingers]
        # cv2.putText(img, f'{str(totalFingers)}', (40, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{(int(fps))}', (400, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)