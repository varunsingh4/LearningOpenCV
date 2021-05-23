import cv2
cap=r"C:\Users\91760\Downloads\production ID_4824397.mp4"
cap=cv2.VideoCapture(cap)
cap.set(10,10000)
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
