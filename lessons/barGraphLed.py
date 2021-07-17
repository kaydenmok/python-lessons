import RPi.GPIO as GPIO
import time
LWAY = 1
MWAY = 2

dataPin = 11
latchPin = 13
clockPin = 15

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dataPin,GPIO.OUT)
    GPIO.setup(latchPin,GPIO.OUT)
    GPIO.setup(clockPin,GPIO.OUT)

def sendout(dPin, cPin, way, val):
    for i in range(8):
        GPIO.output(cPin,GPIO.LOW)
        if(way == LWAY):
            GPIO.output(dPin,(0x01 & (val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        elif(way == MWAY):
            GPIO.output(dPin,(0x80 & (val<<i)==0x80)and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin, GPIO.HIGH)

def loop():
    while True:
        x=0x01
        for i in range(8):
            GPIO.output (latchPin, GPIO.LOW)
            sendout(dataPin, clockPin, LWAY, x)
            GPIO.output(latchPin, GPIO.HIGH)
            x<<=1
            time.sleep(0.05)
        x = 0x80
        time.sleep(0.5)
        for i in range(8):
            GPIO.output(latchPin, GPIO.LOW)
            sendout(dataPin, clockPin, LWAY, x)
            GPIO.output(latchPin, GPIO.HIGH)
            x>>=1
            time.sleep(0.1)
        time.sleep(0.5)

def destroy():
    GPIO.cleanup()

if __name__ =="__main__": 
    print("starting...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()