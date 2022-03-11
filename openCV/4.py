#ROI

import cv2

image = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/cat.jpg')
roi = image[200:350, 50:200]
image[0:150, 0:150] = roi
cv2.imshow("ROI",image)
cv2.waitKey(0) 
