from time import time
from urllib import response
import numpy as np
import cv2
import utils
import requests
import shutil
import time

host = "http://localhost:10000"
url = '/start'


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

with requests.Session() as s:
    answer = ''
    for i in range(0,100):
        start_time = time.time()
        params = {'ans':answer}

        response = s.post(host+url,params)
        print('Server Return: '+response.text)
        if i == 0:
            returned = response.text
            img_url = host + returned
            url = '/check'
        else:
            returned = response.json()
            image_url = host + returned['url']   

        print('Problem ' + str(i) + ': ' + image_url)  

        #특정 폴더에 이미지 파일을 다운함    
        response = s.get(img_url,stream=True)
        target_image = '/.target_images/'+str(i)+'.png'
        with open(target_image,'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response

        #다운로드 받은 이미지 파일을 분석하여 답을 도출함
        answer_string = get_result(target_image)
        print('String: '+answer_string)
        answer_string = utils.remove_first_0(answer_string)
        answer = str(eval(answer_string))
        print('Answer: '+answer)
        print("--- %s second ---" % (time.time() - start_time))

