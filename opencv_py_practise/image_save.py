import cv2
import numpy as np

webcam=cv2.VideoCapture(0)

while True:
	ret,frame=webcam.read()
	cv2.imshow('color',frame)
	k=cv2.waitKey(1)
	if k==113:   #113='q'
		break
	if k==115:   #115='s'
		print("Saving images started")
		for x in xrange(1,20):
			ret,frame=webcam.read()
			cv2.imshow('color',frame)
			cv2.imwrite('test%02d.jpg'%x,frame)
		print("images successfully saved")

webcam.release()
cv2.destroyAllWindows()
