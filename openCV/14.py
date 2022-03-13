#원 그리기
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = np.full((512,512,3),255,np.uint8)
image = cv2.circle(image,(255,255),30,(255,0,0),10)

plt.imshow(image)
plt.show()