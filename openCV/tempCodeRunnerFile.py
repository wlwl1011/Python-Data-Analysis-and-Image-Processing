#이미지 크기 조절 : 이미지를 늘리는데에는 어떻게 추가적으로 픽셀을 추가할지 고민이 필요함. 
# 이 때 Interpolation을 이용한다. -> resize 함수 사용
from configparser import Interpolation
import cv2

image = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/cat.jpg')
cv2.imshow('Original',image)

#cv2.resize(image, dsize, fx, fy, interploation)
expand = cv2.resize(image,None, fx=2.0, fy=2.0, interpolation= cv2.INTER_CUBIC)
cv2.imshow('Expand',expand)

shrink = cv2.resize(image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
cv2.imshow('Shrink',shrink)


