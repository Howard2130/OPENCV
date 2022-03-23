import cv2
import numpy as np

EVT = 0
def cap(event,x,y,flags,param):
    global EVT
    global PNT
    global PNT2
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        print(x,y)
        EVT = event
        PNT = (x,y)
    if event == cv2.EVENT_LBUTTONUP:
        print(event)
        EVT = event
        PNT2 = (x,y)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        print(event)
        EVT = event

cv2.namedWindow('MBS3523')
cv2.setMouseCallback('MBS3523',cap)

cam = cv2.VideoCapture(0)

while True:
    success, img = cam.read()
    cv2.putText(img, 'MBS3523 Assignment 1d – Q6 Name: WONG HO YIN', (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),2)
    if EVT == 4:
        cv2.rectangle(img,PNT,PNT2, (0,255,0), 4)
        img2 = img[PNT[1]:PNT2[1], PNT[0]:PNT2[0]]
        cv2.imshow('img', img2)
    if EVT == 8:
        img[:,:]=img

    cv2.imshow('MBS3523', img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()