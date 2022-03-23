import cv2
import numpy as np

cam = cv2.VideoCapture(0)

def nil(x):
    pass

cv2.namedWindow('MBS3523')

cv2.createTrackbar('CENTER X','MBS3523',320,640,nil)
cv2.createTrackbar('CENTER Y','MBS3523',240,480,nil)

while True:
    success, img = cam.read()
    x = cv2.getTrackbarPos('CENTER X', 'MBS3523')
    y = cv2.getTrackbarPos('CENTER Y', 'MBS3523')
    cv2.line(img, (x, 0), (x, 640), (0, 255, 0), 3)
    cv2.line(img,(0,y),(800,y),(0,255,0),3)
    cv2.putText(img, 'MBS3523 Assignment 1d – Q5 Name: WONG HO YIN',(0,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),2)
    cv2.imshow('MBS3523', img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()