#텍스트 그리기

import cv2
import matplotlib.pyplot as plt
import numpy as np

image = np.full((512,512,3),255,np.uint8)
image = cv2.putText(image,'Hello World',(0,200),cv2.FONT_ITALIC,2,(255,0,0))

plt.imshow(image)
plt.show()