import proxy
from speech import input_floors
# from pi_face_recognition import face_recog
import pi_face_recognition
# import encode_faces
import pickle
import cv2

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
				person_name = pi_face_recognition.face_recog(data, detector)
				print(person_name)
				break
			else:
				print(output)
				count+=1

