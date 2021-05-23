import cv2
import numpy as np
print("Package Imported")
img=r'C:\Users\91760\Downloads\Varun Hidden.png'
cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
cv2.namedWindow("Output1", cv2.WINDOW_NORMAL)
cv2.namedWindow("Output2", cv2.WINDOW_NORMAL)
img=cv2.imread(img)
imgResize=cv2.resize(img,(2500,3500))
imCropped=img[0:200,300:500]
print(img.shape)
print(imgResize.shape)
cv2.imshow('Output2',imCropped)
cv2.imshow('Output',img)
cv2.imshow('Output1',imgResize)

cv2.waitKey(0)