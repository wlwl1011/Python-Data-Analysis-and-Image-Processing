#Thresholding -> 이미지 이진화, 임계점을 기준으로 .. 
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/cat.jpg',cv2.IMREAD_GRAYSCALE)

images = []
ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY) #픽셀 값이 threshold 값보다 크면 value 작으면 0으로 할당
ret, thres2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV) #그것의 반대
ret, thres3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC) #픽셀 값이 threshold 값보다 크면 threshold, 작으면 그대로
ret, thres4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)#픽셀 값이 threshold 값보다 크면 threshold, 작으면 0
ret, thres5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)#픽셀 값이 threshold 값보다 크면 0, 작으면 픽셀 그대로
images.append(thres1)
images.append(thres2)
images.append(thres3)
images.append(thres4)
images.append(thres5)

for i in images:
    plt.imshow(cv2.cvtColor(i,cv2.COLOR_GRAY2RGB))
    plt.show()




