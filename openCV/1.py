import cv2

img_basic = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/cat.jpg',cv2.IMREAD_COLOR) 
cv2.imshow('Image Basic',img_basic)
cv2.waitKey(0) # waitKey : 키보드 입력을 처리하는 함수, time = 0이면 무한 대기
cv2.imwrite('../result1.png',img_basic)

cv2.destroyAllWindows() #창을 닫음

#흑백으로 바꾸기
img_gray = cv2.cvtColor(img_basic,cv2.COLOR_BGR2GRAY) 
cv2.imshow('Image Basic',img_gray)
cv2.waitKey(0) # waitKey : 키보드 입력을 처리하는 함수, time = 0이면 무한 대기
cv2.imwrite('./result2.png',img_gray)