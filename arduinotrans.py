import sys
import serial
import time
import os
import os.path
import random

ser = serial.Serial('/dev/tty.usbmodem1451', 9600)

#fname='C:\\Users\\Ziran\\AppData\\Roaming\\HexChat\\logs\\lastsession.txt'
fname= '/Users//SmrtAsian//Desktop//file.txt'
#fname='/Volumes/BOOTCAMP/Users/Ziran/Desktop/lastsession.txt'
old=0
modeselect=1
one=1
while(1==one):
	while (1==modeselect):
		#print 'swag'
		#print os.path.isfile('/Volumes/BOOTCAMP/Users/')
		try:
			fhand=open(fname,'r')
			
		except:
			print 'Try again:',fname
			exit()
		j=1  
		for line in fhand:
			ser.write(line)
			print (line)
			
		fhand.close()
exit()