#Tracker -> 사용자가 값을 편하게 바꿔볼 수 있도록 해주는 기능

import cv2
import numpy as np

def change_color(x):
    r = cv2.getTrackbarPos("R","Image")
    g = cv2.getTrackbarPos("G","Image")
    b = cv2.getTrackbarPos("B", "Image")
    image[:] = [b,g,r] #RGB를 받아온 후에 backgroud를 칠하겠다.
    cv2.imshow('Image',image)

image = np.zeros((600,400,3),np.uint8)   #unit8 = 부호 없는 8비트 정수형
cv2.namedWindow("Image")

cv2.createTrackbar("R","Image",0,255,change_color)
cv2.createTrackbar("G","Image",0,255,change_color)
cv2.createTrackbar("B","Image",0,255,change_color)

cv2.imshow("Image",image)
cv2.waitKey(0)



