
import cv2
import numpy as np
print("Package Imported")
img=r'C:\Users\91760\Downloads\Varun Hidden.png'
faceCascade=cv2.CascadeClassifier('')
cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
img=cv2.imread(img)
cv2.imshow('Result',img)
cv2.waitKey(0)