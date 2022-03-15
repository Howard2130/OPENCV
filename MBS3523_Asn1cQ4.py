import cv2
print(cv2.__version__)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'Resources/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

while True:
    success , frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray, 1.1, 3)
    for (x,y,w,h) in faces:
        cv2.rectangle(frameGray, (x,y),(x+w,y+h),(0,0,255),3)
    cv2.putText(frame, 'MBS3523 Assignment 1c – Q4    Name: WONG HO YIN', (1, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 2)
    cv2.putText(frameGray, 'MBS3523 Assignment 1c – Q4    Name: WONG HO YIN', (1, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 2)
    cv2.imshow('MBS3523-GRAY', frameGray)
    cv2.imshow('MBS3523', frame)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()