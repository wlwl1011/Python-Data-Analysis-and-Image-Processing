#다각형 그리기

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512,512,3),255,np.uint8)
points = np.array([[5,5],[128,128],[483,444],[400,150]])
image = cv2.polylines(image,[points],True,(0,0,255),4)

plt.imshow(image)
plt.show()