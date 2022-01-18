""" 
Automatic Cat Feeder

Joses Galdamez - jgaldamez102@gmail.com

"""

import sys
import datetime
import grovepi
import grove_rgb_lcd as lcd
import RPi.GPIO as GPIO

sys.path.append('home/pi/Dexter/GrovePi/Software/Python')

#initalizing Devices
PORT_BUZZER = 2 #for D2 on the buzzer
grovepi.pinMode(PORT_BUZZER, "OUTPUT")

def init():
    #initalize the display of the LCD
    lcd.setRGB(224,255,255) # cool blue color
    grovepi.digitalWrite(PORT_BUZZER, 0)# to initalize it turn off
    GPIO.setmode(GPIO.BOARD)
    #current time 
    while True:
        currTime = datetime.datetime.now()
        #writing the current time on the LCD screen
        lcd.setText_norefresh("Time: " + str(currTime))
        currTimeHour = currTime.hour
        currTimeMinute = currTime.minute
        currTimeSecond = currTime.second
        print(currTimeSecond)
        # print(currTime)
        #if the it hits a new
        if (currTimeSecond ==0):
            grovepi.digitalWrite(PORT_BUZZER, 1)
            lcd.setText("FEEDING TIME")
        else:
            grovepi.digitalWrite(PORT_BUZZER, 0)
            lcd.setText_norefresh("Time: " + str(currTime)) 
        
    return 
if __name__ == "__main__":
    init()
