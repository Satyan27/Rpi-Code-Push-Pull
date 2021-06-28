import proxy
from speech import input_floors
from pi_face_recognition import face_recog
import encode_faces

while(1):
	if proxy.proxy_detection() == True:
		call = input_floors
		if call == True:
			face_recog()
		else:
			pass
