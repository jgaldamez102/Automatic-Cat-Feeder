""" 
Automatic Cat Feeder

Joses Galdamez - jgaldamez102@gmail.com

"""

import sys
import datetime
import grovepi
import grove_rgb_lcd as lcd
import RPi.GPIO as GPIO
import time

sys.path.append('home/pi/Dexter/GrovePi/Software/Python')

#initalizing Devices
PORT_BUZZER = 2 #for D2 on the buzzer
grovepi.pinMode(PORT_BUZZER, "OUTPUT")

def stepper(control_pins):
    halfstep_seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
        ]
    for i in range(512):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            # time.sleep(0.001)

def init():
    #initalize the display of the LCD
    lcd.setRGB(224,255,255) # cool blue color
    grovepi.digitalWrite(PORT_BUZZER, 0)# to initalize it turn off
    GPIO.setmode(GPIO.BOARD) #setting up the pins 
    control_pins = [7,11,13,15]
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
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
            stepper(control_pins) #calling stepper function
            lcd.setText("FEEDING TIME")
        else:
            grovepi.digitalWrite(PORT_BUZZER, 0)
            lcd.setText_norefresh("Time: " + str(currTime)) 

        
    return 
if __name__ == "__main__":
    init()
