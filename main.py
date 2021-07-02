import proxy
from speech import input_floors
from pi_face_recognition import face_recog
import pickle
import cv2
from temp_recording import temperature
import csv
from datetime import datetime

print("[INFO] loading encodings + face detector...")
data = pickle.loads(open("encodings.pickle", "rb").read())
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(1):
	if proxy.proxy_detection() == True:
		count = 0
		while(count<3):
			status, output = input_floors()
			if status == True:
				print(output)
				person_name = face_recog(data, detector)
				temp = temperature()
				print(person_name, temp)
				fields=[person_name, temp, output, datetime.now()]
				with open('database.csv', 'a') as f:
				    writer = csv.writer(f)
				    writer.writerow(fields)
				break
			else:
				print(output)
				count+=1

