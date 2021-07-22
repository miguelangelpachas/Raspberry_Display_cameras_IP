import RPi.GPIO as GPIO
import time
import os
import random

from io import open
enable='sudo systemctl enable displaycameras.service'
start='sudo systemctl start displaycameras.service'
stop='sudo systemctl stop displaycameras.service'
start2='omxplayer -o hdmi --live rtsp://admin:ford2019@192.168.1.64:554/videoMain'
start3='omxplayer -o hdmi --live rtsp://admin:Hik12345@192.168.1.120:554/videoMain'
os.system(enable)
#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
		pin19=GPIO.input(19)
		pin26=GPIO.input(26)
		BNO55=GPIO.input(16)
		os.system(start)

		if BNO55==False:
		   print("  Posicion correcta")
		   os.system(start)

		#if pin19!=False and pin26==False:
                  # os.system(stop)
                  # os.system(start2)
		   

		#if pin26!=False and pin19==False:
		  # print("Derecha")
                  # os.system(stop)
                  # os.system(start3)

		#if pin19!=True and pin26!=True:
		  # print("Pantalla dividida");
                  # os.system(start)
                 
                #if pin19==True and pin26==True:
		   #os.system(start)
                
		if BNO55==True:
		   print("  Posicion Incorrecta")
		   os.system(start)  

		   

