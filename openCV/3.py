import cv2
import time

image = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/openCV/cat.jpg')

start_time = time.time()
for i in range(0,100):
    for j in range(0,100):
        image[i,j] = [255,255,255]

print("--- %s seconds --- " % (time.time()-start_time))
#cv2.imshow("Image1", image)

start_time1 = time.time()
image[0:100, 0:100] = [0, 0, 0]
print("--- %s seconds --- " % (time.time()-start_time1))

#cv2.imshow("Image2", image)
#cv2.waitKey(0) 




