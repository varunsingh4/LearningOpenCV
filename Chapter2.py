import cv2
import numpy as np
img=r'C:\Users\91760\Downloads\Varun Hidden.png'
img=cv2.imread(img)
kernel=np.ones((5,5),np.uint8)
cv2.namedWindow("Gray", cv2.WINDOW_NORMAL)
imGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Blur", cv2.WINDOW_NORMAL)
cv2.namedWindow("Canny", cv2.WINDOW_NORMAL)
cv2.namedWindow("Dilation", cv2.WINDOW_NORMAL)
cv2.namedWindow("Erosion", cv2.WINDOW_NORMAL)
imBlur=cv2.GaussianBlur(imGray,(7,7),0)
imCanny=cv2.Canny(img,200,300)
imDilation=cv2.dilate(imCanny,kernel,iterations=1)
imEroded=cv2.erode(imDilation,kernel,iterations=1)
cv2.imshow("Gray",imGray)
cv2.imshow('Blur',imBlur)
cv2.imshow('Canny',imCanny)
cv2.imshow('Dilation',imDilation)
cv2.imshow('Erosion',imEroded)

cv2.waitKey(0)