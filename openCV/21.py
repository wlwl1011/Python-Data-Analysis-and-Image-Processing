#Filtering

import numpy as np
import cv2

image = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/digit_image.png')

size = 4
#kernel = np.ones((size,size),np.float32) / (size**2)

#print(kernel)

#dst = cv2.filter2D(image, -1, kernel)
#dst = cv2.blur(image,(4,4))
dst = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('Image',dst)
cv2.waitKey(0) 
