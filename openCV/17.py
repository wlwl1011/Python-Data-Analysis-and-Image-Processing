#Contour(외곽): 어떠한 사물의 테두리를 구분하고자 할 때..

import cv2
import matplotlib.pyplot as plt
image = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/gray_image.jpg')
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray,127,255,0)

#plt.imshow(cv2.cvtColor(thresh,cv2.COLOR_GRAY2RGB))
#plt.show()

#index 1이 모든 contour의 정보를 담고 있다.
contours, _ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)
#-1을 했으니 그것을 모두 출력해라!

image = cv2.drawContours(image, contours, 1, (255,0,0),3)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()