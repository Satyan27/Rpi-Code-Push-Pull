import speech_recognition as sr


def speech_to_text():
	# Record Audio
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("[+] Enter Floor Number")
	    audio = r.listen(source)

	# Speech recognition using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    print("[+] Command: " + r.recognize_google(audio))
	except sr.UnknownValueError:
	    print("[-] Google Speech Recognition could not understand audio")
	    speech_to_text()
	except sr.RequestError as e:
	    print("[-] Could not request results from Google Speech Recognition service; {0}".format(e))
	    speech_to_text()
	return r.recognize_google(audio)

floors = {
	"ground floor": 0,
	"zero": 0,
	"1st floor": 1,
	"first floor": 1,
	"one": 1,
	"2nd floor": 2,
	"second floor": 2,
	"two": 2,
	"3rd floor": 3,
	"third floor": 3,
	"three": 3,
	"4th floor": 4,
	"fourth floor": 4,
	"four": 4,
	"5th floor": 5,
	"fifth floor": 5,
	"five": 5,
	"6th floor": 6,
	"sixth floor": 6,
	"six": 6,
	"7th floor": 7,
	"seventh floor": 7,
	"seven": 7,
	"8th floor": 8,
	"eighth floor": 8,
	"eight": 8,
	"9th floor": 9,
	"ninth floor": 9,
	"nine": 9,
	"10th floor": 10,
	"tenth floor": 10,
	"ten": 10,
}	

def input_floors():
	x = speech_to_text()
			if x in floors:
				print(x)
				return x
			else 
				print("[-] Invalid Command. Try Again")
				input_floors()