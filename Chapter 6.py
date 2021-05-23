import cv2
import numpy as np
img=r'C:\Users\91760\Downloads\Varun Hidden.png'
img=cv2.imread(img)
cv2.namedWindow("Output1", cv2.WINDOW_NORMAL)
cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
img=np.hstack((img,img))
imgVer=np.vstack((img,img))
cv2.imshow('Output',img)
cv2.imshow('Output1',imgVer)

cv2.waitKey(0)