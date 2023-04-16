import cv2
import numpy as np

# Read the image 
img = cv2.imread('image.jpg',0)

# Find the maximum grayscale value 
max_gray = np.max(img) 

# Get the index of max grayscale pixel
idx = np.where(img == max_gray)  

# Display the coordinate of max grayscale pixel 
font = cv2.FONT_HERSHEY_SIMPLEX 
str = '(' + str(idx[1][0]) + ',' + str(idx[0][0]) + ')'
cv2.putText(img, str, (idx[1][0],idx[0][0]), font,  
                    1, (0,255,0), 2, cv2.LINE_AA)

# Display the image
cv2.imshow('Image', img) 
cv2.waitKey(0)
