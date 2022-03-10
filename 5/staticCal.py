import numpy as np

#행렬 상수 곱셈
array = np.random.randint(1,10,size=4).reshape(2,2)
print(array)
result_array = array *10
print(result_array)

#행렬 덧셈 - 브로드 캐스트 : 형태가 다른 배열을 연산 할 수 있도록 배열의 형태를 동적으로 변환
array1 = np.arange(4).reshape(2,2)
array2 = np.arange(2)

array3 = array1 + array2
print(array3)

array4 = np.arange(0,8).reshape(2,4)
array5 = np.arange(0,8).reshape(2,4)
array6 = np.concatenate([array4, array5],axis=0)
array7 = np.arange(0,4).reshape(4,1)

print(array6 + array7)

#마스킹 연산
array8 = np.arange(16).reshape(4,4)
print(array8)

array9 = array8 < 10
print(array9)

array8[array9] = 100
print(array8) #색상에 너무 밝거나 할 때 수정 할 수 있다. 조건문 보다 마스킹 연산이 더 빠르다.

#최대 최소 합 평균
print("최대 최소 합 평균")
array9 = np.arange(16).reshape(4,4)
print("최댓값:",np.max(array9))
print("최솟값:",np.min(array9))
print("합계:",np.sum(array9))
print("평균값:",np.mean(array9))
