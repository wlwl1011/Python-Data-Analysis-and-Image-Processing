#유사 다각형 구하기

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/digit_image.png')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray,230,255,0)
#배경과 숫자의 bit 반전 -> 찾아야 할 객체는 흰색이어야 하고 배경은 검정색이어야 한다.

thresh = cv2.bitwise_not(thresh)

plt.imshow(cv2.cvtColor(thresh,cv2.COLOR_GRAY2RGB))
plt.show()

#index 1이 모든 contour의 정보를 담고 있다.
contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(contours)
#-1을 했으니 그것을 모두 출력해라!
image = cv2.drawContours(image, contours, -1, (255,0,0),3)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

contour = contours[2]
epsilon = 0.01 * cv2.arcLength(contour,True)
approx = cv2.approxPolyDP(contour,epsilon,True)
image = cv2.drawContours(image,[approx],-1, (0,0,255),3)

plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.show() 