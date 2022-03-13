#직선 그리기

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512,512,3),255,np.uint8)
image = cv2.line(image,(0,0),(255,255),(255,0,0),10)

plt.imshow(image)
plt.show()