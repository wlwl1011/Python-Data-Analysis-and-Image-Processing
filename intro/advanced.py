import numpy as np

#단일 객체 저장 및 불러오기
array = np.arange(0,10)
np.save('saved.npy',array)#array 함수를 saved.npy 파일로 저장
result = np.load('saved.npy')
print(result)

#복수 객체 저장 및 불러오기
array1 = np.arange(0,10)
array2 = np.arange(10,20)
np.savez('saved.npz',array1=array1, array2=array2)
data = np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']
print(data)
print(result1)
print(result2)

#Numpy 원소 오름차순 정렬
array3 = np.array([5,9,10,3,1])
array3.sort()
print(array3)
#내림차순
print(array3[::-1])

#각 열을 기준으로 정렬
array4 = np.array([[5,9,10,3,1],[8,3,4,2,5]])
print(array4)
array4.sort(axis = 0)
print(array4)

#균일한 간격으로 데이터 생성
array5 = np.linspace(0,10,5)#0부터 10까지 5개의 데이터를 일정한 간격으로 생성
print(array5)

#난수의 재연 (실행마다 결과 동일)
np.random.seed(7)
print(np.random.randint(0,10,(2,3)))

#Numpy 배열 객체 복사
array6 = np.arange(0,10)
array7 = array1
array7[0] = 99 #array1과 array2가 같은 주소를 가르키고 있기 때문에 array1의 결과도 수정
print(array1)

#따라서 그냥 = 기호를 통해서 값을 복사하는 것을 좋지 못함
array8 = np.arange(0,10)
array9 = array8.copy()
array9[0] = 99  
print(array8)

#중복된 원소 제거
array10 = np.array([1,1,2,2,2,3,3,4])
print(np.unique(array10))