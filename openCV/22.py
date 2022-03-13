#KNN 알고리즘 - k'개의 다른 데이터의 레이블을 참조하여 분류하는 알고리즘으로 거리를 측정할 때 유클리디안 거리 계산법을 사용
import cv2
import numpy as np
from matplotlib import pyplot as plt

#각 데이터의 위치 지정
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
#각 데이터 label 지정
response = np.random.randint(0,2,(25,1)).astype(np.float32)

#값이 0인 데이터를 각각 (x,y) 위치에 빨간색으로 칠함
red = trainData[response.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')

#값이 1인 데이터를 각각 (x,y) 위치에 파랑으로 칠함
blue = trainData[response.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

#새로운 하나의 데이터 생성
newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE,response)
ret, result, neighbours, dist = knn.findNearest(newcomer,3)

print("result",result)
print("neighbours",neighbours)
print("dist",dist)#이웃 데이터에 대한 거리

plt.show()

