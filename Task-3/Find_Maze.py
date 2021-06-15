# import the necessary packages
import numpy as np
import argparse
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

# load the image
image = cv2.imread("C:/Research Group/maze_lv3.png")
boundaries = [([230, 0, 0], [230, 255, 255])]
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
	cv2.imshow("images", output)
	cv2.imwrite('C:/Research Group/New.jpg',output)
	





   
cv2.waitKey(0)
