import cv2
import numpy as np
method = cv2.TM_SQDIFF_NORMED


# Read the images from the file
small_image = cv2.imread('C:/Research Group/Saved Image.png')
large_image = cv2.imread('C:/Research Group/zucky_elon.png')

result = cv2.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(60,76,231),2)

# Display the original image with the rectangle around the match.
cv2.imshow('output',large_image)

start_point=[60,76,231]
# Get X and Y coordinates of all blue pixels
X,Y = np.where(np.all(large_image==start_point,axis=2))
print(X,Y)
large_image[459,230]=(255,0,0)
cv2.imshow("Change", large_image)
# The image is only displayed if we call this
cv2.waitKey(0)