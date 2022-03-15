#Adaptive Thresholding -> 적응 임계점 처리
#이렇게(Global Threshold) 하면 음영이 다르면 일부 영역이 모두 흰색 또는 검정색으로 보여지게 됨. 
#즉, 버려지는 영역이 많아짐.  
#이 문제를 처리하기 위해 이미지의 작은 영역별로 나누어 Thresholding 을 하는 것이 Adaptive Threshold 이다.

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/cat.jpg',cv2.IMREAD_GRAYSCALE)

ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
thres2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,21,3)

plt.imshow(cv2.cvtColor(image,cv2.COLOR_GRAY2RGB))
plt.show()


plt.imshow(cv2.cvtColor(thres1,cv2.COLOR_GRAY2RGB))
plt.show()

plt.imshow(cv2.cvtColor(thres2,cv2.COLOR_GRAY2RGB))
plt.show()