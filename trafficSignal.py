import RPi.GPIO as GP #General Purpose I/O
import time

'''
	R : 7,
	G : 13,
	Y : 15
	
	R : 29,
	G : 31,
	Y : 33
	
	R : 37,
	G : 36,
	Y : 32
	
	R : 22,
	G : 18,
	Y : 16
'''

def init(r,g,y):
	GP.setmode(GP.BOARD)		#GP.BOARD => Pin no on Board and GP.BCM => GPIO number
	GP.setup(r,GP.OUT)
	GP.setup(g,GP.OUT)
	GP.setup(y,GP.OUT)
	GP.output(r,GP.HIGH)

def startSignal(r,g,y):
	GP.output(r,GP.LOW)
	GP.output(g,GP.HIGH)
	time.sleep(5)
	GP.output(g,GP.LOW)
	GP.output(y,GP.HIGH)
	time.sleep(2)
	GP.output(y,GP.LOW)
	GP.output(r,GP.HIGH)
	


def trafficSignal():
	
	init(7,13,15)
	init(29,31,33)
	init(37,36,32)
	init(22,18,16)
	
	while(True):
		startSignal(7,13,15)
		time.sleep(0.5)
		startSignal(29,31,33)
		time.sleep(0.5)
		startSignal(37,36,32)
		time.sleep(0.5)
		startSignal(22,18,16)
		time.sleep(0.5)
		
trafficSignal()
