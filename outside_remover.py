import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import time

model = keras.models.load_model('/Users/praharshgurudatta/Documents/5th_sem/Project/inside_outside.h5')


def predictImage(frame):
	y = image.img_to_array(frame)
	x = np.expand_dims(y,axis=0)
	val = model.predict(x)
	if val == 1:
		return 'inside'
	elif val == 0:
		return 'outside'


video = '/Users/praharshgurudatta/Downloads/My_Videos/202109080914_45_1.mp4'
output = '/Users/praharshgurudatta/Documents/output.mp4'
frame_rate = 30

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output, fourcc, frame_rate, (640,480))

video_capture = cv2.VideoCapture(video)


while video_capture.isOpened():

	ret, frame = video_capture.read()

	if ret:
		# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# cv2.imshow('frame', gray)
		# if cv2.waitKey(1) == ord('q'):
		# 	break
		frame = cv2.resize(frame, (150, 150))
		res = predictImage(frame)
		if res == 'inside':
			out.write(frame)
		else:
			continue

out.release()
video_capture.release()