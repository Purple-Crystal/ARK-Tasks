import cv2 as cv

# Read image from your local file system
original_image = cv.imread('C:/Users/admin/Pictures/Screenshots/Screenshot (100).png')

# Convert color image to grayscale for Viola-Jones
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
detected_faces = face_cascade.detectMultiScale(grayscale_image)
for (column, row, width, height) in detected_faces:
    cv.rectangle( original_image,(column, row),(column + width, row + height),(255, 255, 255), 2)
cv.imshow('Image', original_image)
cv.waitKey(0)
cv.destroyAllWindows()