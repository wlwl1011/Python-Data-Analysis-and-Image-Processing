import numpy as np
import cv2
import utils

FILE_NAME = '/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/CaptchaHacking/Kmodel/trained.npz'

with np.load(FILE_NAME) as data:
    train = data['train']
    train_labels = data['train_labels']

knn = cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE,train_labels)

def check(test,train,train_labels):
    ret, result, neighbours, dist = knn.findNearest(test,k=1)
    return result

def get_result(file_name):
    image = cv2.imread(file_name)
    chars = utils.extract_chars(image)
    result_string = ""
    for char in chars:
        matched = check(utils.resize20(char[1]), train, train_labels)
        if matched < 10:
            result_string += str(int(matched))
            continue
        elif matched == 10:
            matched = "+"
        elif matched == 11:
            matched = "-"
        elif matched == 12:
            matched = "*"
        result_string += matched
    return result_string

print(get_result('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/CaptchaHacking/Kmodel/images/5.png'))            

