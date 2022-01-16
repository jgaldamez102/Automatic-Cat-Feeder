""" 
Automatic Cat Feeder

Joses Galdamez - jgaldamez102@gmail.com

"""

import sys
import datetime
import grovepi
import grove_rgb_lcd as lcd

sys.path.append('home/pi/Dexter/GrovePi/Software/Python')

#initalizing Devices
PORT_BUZZER = 2 #for D2 on the buzzer
grovepi.pinMode(PORT_BUZZER, "OUTPUT")

def init():
    #initalize the display of the LCD
    lcd.setRGB(224,255,255) # cool blue color
    grovepi.digitalWrite(PORT_BUZZER, 0)# to initalize it turn off
    #current time 
    while True:
        currTime = datetime.datetime.now()
        currTimeHour = currTime.hour
        currTimeMinute = currTime.minute
        currTimeSecond = currTime.second
        print(currTimeSecond)
        # print(currTime)
        #if the it hits a new
        if (currTimeSecond >= 0 and currTimeSecond < 1):
=======
        if (currTimeSecond >= 0 and currTimeSecond <= 2):
>>>>>>> ebfdae43a9cc7cfad309e11308b987e954924db5
            grovepi.digitalWrite(PORT_BUZZER, 1)
        else:
            grovepi.digitalWrite(PORT_BUZZER, 0)
        
    return 
if __name__ == "__main__":
    init()
