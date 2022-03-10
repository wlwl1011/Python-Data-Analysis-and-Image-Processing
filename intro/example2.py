import numpy as np

#배열 합치기
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.concatenate([array1,array2])

print(array3.shape)
print(array3)

#배열 형태 바꾸기
array4 = np.array([1,2,3,4])
array5 = array4.reshape((2,2))

print(array5)
print(array5.shape)

#배열 합치기2
array6 = np.arange(4).reshape(1,4) #0부터 3까지 데이터를 만들고 2차원 배열로 만들어줌
print(array6)
array7 = np.arange(8).reshape(2,4) #0부터 7까지 데이터를 만들고 2차원 배열로 만들어줌
print(array7)
array8 = np.concatenate([array6,array7],axis=0) #행을 기준으로 덧붙임
print(array8)