import cv2
import numpy as np
img=r'C:\Users\91760\Downloads\Cards.jfif'
img=cv2.imread(img)
width,height=250,350
pts1=np.float32([[257,88],[309,86],[260,155],[307,156]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow('Output1',imgOutput)
cv2.imshow('Output',img)
cv2.waitKey(0)