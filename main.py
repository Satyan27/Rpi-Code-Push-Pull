import proxy
from speech import floors, speech_to_text
# import pi_face_recognition
# import encode_faces

while(1):
	if proxy.dummy() == True:
		x = speech_to_text()
		if x in floors:
			print(x)
		else:	
			print('[-] Invalid input. Try again.')
	# else:
	# 	pass