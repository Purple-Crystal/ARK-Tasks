from tkinter import *
from PIL import ImageTk, Image
import cv2


root = Tk()
# Create a frame
app = Frame(root, bg="white")
app.grid()
# Create a label in the frame
lmain = Label(app)
lmain.grid()

cascPath ="haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# Capture from camera
cap = cv2.VideoCapture(0)

# function for video streaming
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    
    while True:



     faces = faceCascade.detectMultiScale(cv2image,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)

    # Draw an ellipse around the faces
     for (x, y, w, h) in faces:
        cenx = x + w//2
        ceny = y + h//2
        center = (cenx,ceny)
        cv2.ellipse(frame, center, (w-50, h-50), 0, 0, 360, (255, 255, 0), 4)
        faces = frame[y:y + h, x:x + w]
    # Display the resulting frame
     cv2.imshow('Video', frame)
   
     lmain.after(1, video_stream) 
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break
     

video_stream()
root.mainloop()