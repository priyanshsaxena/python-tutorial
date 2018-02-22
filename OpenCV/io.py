# importing cv2
# images are loaded as numpy arrays

import numpy as np
import cv2

'''
The flags for reading

cv2.IMREAD_COLOR : (Default) Loads a color image. Representation = -1
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode. Representation = 0
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel. Representation = 1

Representation integer can be used insteas of using the whole flag-name
'''


# Load an color image in grayscale
img = cv2.imread('messi5.jpg',0)

# Save as a png image
cv2.imwrite('messigray.png',img)