import RPi.GPIO as GPIO
import time
LWAY = 1
MWAY = 2
dataPin = 11
latchPin = 13
clockPin = 15

num = [0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90,0x88,0xc6,0xa1,0x86,0x8e]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(dataPin,GPIO.OUT)
    GPIO.setup(latchPin,GPIO.OUT)
    GPIO.setup(clockPin,GPIO.OUT)

def sendout(dPin,cPin,way,val):
    for i in range (0,8):
        GPIO.output(cPin,GPIO.LOW)
        if(way == LWAY):
            GPIO.output(dPin, (0x01 & (val>>i) ==0x01)and GPIO.HIGH or GPIO.LOW)
        elif(way == MWAY):
            GPIO.output(dPin,(0x80 & (val<<i)==0x80)and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin,GPIO.HIGH)


def loop():
    for i in range(0,len(num)):
         GPIO.output(latchPin, GPIO.LOW)
         sendout(dataPin, clockPin, MWAY, num[i])
         GPIO.output(latchPin, GPIO.HIGH)
         time.sleep(0.5)
    for i in range(0,len(num)):
         GPIO.output(latchPin,GPIO.LOW)
         sendout(dataPin,clockPin,MWAY,num[i]&0x7f)
         GPIO.output(latchPin, GPIO.HIGH)
         time.sleep(0.5)
        
def destroy():
    GPIO.cleanup()

if __name__=='__main__':
    print("starting...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()        





