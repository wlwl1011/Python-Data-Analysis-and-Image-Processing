#이미지 회전

import cv2
import numpy as np

image = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/cat.jpg')

height, width = image.shape[:2]
print(image.shape)
print(image.shape[:2])

M = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)
dst = cv2.warpAffine(image,M,(width,height))

#cv2.imshow('Hi',dst)
#cv2.waitKey(0)