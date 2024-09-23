import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

while True:
    rec, frame = cap.read()
    frame_gr = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gr, 1.3, 5)
    for x, y, w, h in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 252), 2)
    cv.imshow('frame', frame)

    keyexit = cv.waitKey(5) & 0xFF
    if keyexit == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

