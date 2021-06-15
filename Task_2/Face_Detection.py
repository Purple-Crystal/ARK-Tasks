import cv2
import sys
 
cascPath = "haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
 
video_capture = cv2.VideoCapture(0)
 
while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame,1)
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    faces = faceCascade.detectMultiScale(frame, 1.1, 4)
 
    for (x, y, w, h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 255, 255), 4)
 
    cv2.imshow('Video', frame)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()