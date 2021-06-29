import smbus 
import time 
import datetime 

bus = smbus.SMBus(1) 

#I2C address of sensor
address = 0x48 

def temperature(): 
	rvalue0 = bus.read_word_data(address,0)
	rvalue1 = (rvalue0 & Oxff00) >> 8
	rvalue2 = rvalue0 & Ox0Off 
	rvalue = (((rvalue2 * 256) + rvaluel) >> 4 ) *.0625 
	return rvalue 