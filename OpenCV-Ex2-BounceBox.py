import cv2

print(cv2.__version__)

capture = cv2.VideoCapture(0)

capture.set(3,640)
capture.set(4,480)

x = 0
dx = 10
y = 0
dy = 10

while True:
    success, img = capture.read()
    cv2.rectangle(img, (x, y+100), (x + 50, y+150), (0, 255, 0), 3)

    x = x + dx
    if x >= 600 or x <= 0:
        dx = dx * (-1)

    y = y + dy
    if y >=350 or y <=0:
        dy = dy * (-1)

    cv2.putText(img, 'MBS3523 Name: WONG HO YIN', (1, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 2)

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()