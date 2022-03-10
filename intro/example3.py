import numpy as np

#배열 나누기
array = np.arange(8).reshape(2,4)
left, right = np.split(array, [2], axis =1 ) #index 2를 기준으로 (열)로 나눈다.
print(left.shape)
print(right.shape)
print(array)
print(left)
print(right)
