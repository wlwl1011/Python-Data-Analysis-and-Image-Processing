import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

FILE_NAME = '/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/trained.npz'

#파일로 부터 학습 데이터를 불러옴
def load_train_data(file_name):
    with np.load(file_name) as data:
        train = data['train']
        train_labels = data['train_labels']
    return train, train_labels

#손 글씨 이미지를 (20*20) 크기로 Scaling 한다. -> 크기 맞춤
def resize20(image):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray_resize = cv2.resize(gray,(20,20))
    plt.imshow(cv2.cvtColor(gray_resize, cv2.COLOR_GRAY2RGB))
    plt.show()

    return gray_resize.reshape(-1,400).astype(np.float32)

def check(test, train, train_labels):
    knn = cv2.ml.KNearest_create()
    knn.train(train,cv2.ml.ROW_SAMPLE,train_labels)
    ret, result, neighbours, dist = knn.findNearest(test, k=5)
    return result

train, train_labels = load_train_data(FILE_NAME)

for fime_name in glob.glob('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/test_1.png'):
    test = resize20(fime_name)
    result = check(test, train, train_labels)
    print(result)



