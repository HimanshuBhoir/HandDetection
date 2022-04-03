import cv2
import time
import os
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)

fldrPath = "Fingers"
myList = os.listdir(fldrPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{fldrPath}/{imPath}')
    # print(f'{fldrPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))

pTime = 0

while True:
    success, img = cap.read()

    h, w, c = overlayList[1].shape
    img[0:h, 0:w] = overlayList[1]

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS : {int(fps)}', (300, 70, cv2.FONT_HERSHEY_PLAIN), 1, (255, 0, 0), 1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)