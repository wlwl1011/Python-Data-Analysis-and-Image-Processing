import cv2
import utils

image = cv2.imread('/Users/gimminji/Desktop/2022/Python-Data-Analysis-and-Image-Processing/CaptchaHacking/Kmodel/images/1.png',cv2.IMREAD_COLOR)
blue = utils.get_chars(image.copy(),utils.BLUE)
red = utils.get_chars(image.copy(),utils.RED)
green = utils.get_chars(image.copy(),utils.GREEN)

cv2.imshow('Image Gray',blue)
cv2.waitKey(0)
cv2.imshow('Image Gray',green)
cv2.waitKey(0)
cv2.imshow('Image Gray',red)
cv2.waitKey(0)

