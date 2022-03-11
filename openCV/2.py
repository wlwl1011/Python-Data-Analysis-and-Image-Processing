import cv2

#이미지 크기 및 픽셀 확인
image = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/cat.jpg')
#픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

#이미지 Numpy 객체의 특정 픽셀을 가리킴
px = image[100,100]

#BGR 순서로 출력
print(px)

print(px[2])