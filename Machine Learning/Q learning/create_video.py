import cv2
import os

def make_video():
	fourcc = cv2.VideoWriter_fourcc(*"XVID")
	out = cv2.VideoWriter("data/qlean.avi", fourcc, 30, (1200, 900))

	for i in range(0, 4001, 20):
		img_path = f"data/q_tables/{i}.png"
		frame = cv2.imread(img_path)
		out.write(frame)

	out.release()

make_video()