#OpenCV를 활용한 픽셀별 색상 다루기

import cv2

image = cv2.imread("/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/cat.jpg")
image[:,:,2] = 0 # 0: B , G:1, R:2

cv2.imshow("None red",image)
cv2.waitKey(0)
