import cv2
import numpy as np

webcam=cv2.VideoCapture(0)

while True:
	ret,frame=webcam.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	cv2.imshow('gray',gray)
	cv2.imshow('color',frame)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

webcam.release()
cv2.destroyAllWindows()
