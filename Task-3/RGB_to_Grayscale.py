import cv2
  
originalImage = cv2.imread('C:/Research Group/Moon.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 50, 255,cv2.THRESH_BINARY)
print("Hello")
cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imshow('Original image',originalImage)
cv2.imshow('Gray image', grayImage)
cv2.imwrite('C:/Research Group/Sun.jpg',blackAndWhiteImage)
  
cv2.waitKey(0)
cv2.destroyAllWindows()