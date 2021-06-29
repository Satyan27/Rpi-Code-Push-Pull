import RPi.GPIO as GPIO
import time

def proxy_detection():
  print("Distance Measurement In Progress")

  while(1):
    GPIO.setmode(GPIO.BCM)

    TRIG = 23
    ECHO = 24

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    print("Waiting For Sensor To Settle")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time() 

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    if (distance < 15.0):
      print("Distance:",distance,"cm")
      GPIO.cleanup()

      return True

def dummy():
  count = 12
  while(1):
    print(count)
    if count == 15:
      return True
    count+=1