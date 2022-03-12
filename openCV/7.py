#이미지 위치 변경
import cv2
import numpy as np

image = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/cat.jpg')

height, width = image.shape[:2]
#x= 열 이동 y = 행이동
M = np.array([[1,0,50],[0,1,10]],dtype=np.float32)
dst = cv2.warpAffine(image,M,(width,height))

cv2.imshow('image',dst)
cv2.waitKey(0)

