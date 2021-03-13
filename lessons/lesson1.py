# Using Morse Code to display "Kayden"
# Using function

import RPi.GPIO as GPIO

import time

ledPin = 15

def setup():
    
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(ledPin, GPIO.OUT)
    
    GPIO.output(ledPin, GPIO.LOW)
    
    print ("using pin", ledPin)

def ledOn(seconds = 1):
    
    GPIO.output(ledPin, GPIO.HIGH)
    
    time.sleep(seconds)
    
    GPIO.output(ledPin, GPIO.LOW)
    
    time.sleep(seconds)

  
def loop():
    count = 0
    while count < 2:
        print(count)
        
        #k 
        ledOn(3)

        ledOn(1)

        ledOn(3)
        #a
        ledOn(1)

        ledOn(3)
        #y
        ledOn(3)

        ledOn(1)

        ledOn(3)

        ledOn(3)
        #d
        ledOn(3)

        ledOn(1)

        ledOn(1)
        #e
        ledOn(1)
        #n
        ledOn(3)

        ledOn(1)
        
        count = count + 1
        
def destroy():
    
    GPIO.output(ledPin, GPIO.LOW)
    
    GPIO.cleanup()
    
if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()






