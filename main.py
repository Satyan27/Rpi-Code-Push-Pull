import proxy
from speech import input_floors
from pi_face_recognition import face_recog
import encode_faces

while(1):
	if proxy.proxy_detection() == True:
		count = 0
		while(count<3):
			status, output = input_floors()
			if status == True:
				print(output)
				#face_recog()
				break
			else:
				print(output)
				count+=1

