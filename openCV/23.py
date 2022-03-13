#KNN 숫자 인식

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/digits.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#사진을 세로 50 가로 100으로 나눔
cells = [np.hsplit(row, 100) for row in np.vsplit(gray,50)]
x = np.array(cells)

#각 20*20의 크기의 사진을 한줄로 바꾼다.
train = x[:,:].reshape(-1,400).astype(np.float32) #총 12개의 원소가 들어있는 배열 x에 대해서 x.reshape(-1, 정수) 를 해주면 '열(column)' 차원의 '정수'에 따라서 12개의 원소가 빠짐없이 배치될 수 있도록 '-1'이 들어가 있는 '행(row)' 의 개수가 가변적으로 정해짐을 알 수 있습니다.  

k =np.arange(10)
train_labels = np.repeat(k, 500)[:, np.newaxis]#numpy.repeat 함수는 어레이의 요소들을 지정한 횟수만큼 반복합니다. a = np.repeat(3, 4) -> 3 3 3 3
# np.newaxis 는 차원을 늘리는 것임

np.savez("trained.npz",train=train, train_labels=train_labels)#학습 시킴

plt.imshow(cv2.cvtColor(x[0,0],cv2.COLOR_GRAY2RGB))
plt.show()
cv2.imwrite('test_0.png',x[0,0])
cv2.imwrite('test_1.png',x[5,0])

