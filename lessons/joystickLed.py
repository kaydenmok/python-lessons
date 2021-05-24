import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus=smbus.SMBus(1)
cmd=0x40
ledPin = 6
led2Pin = 19
led3Pin = 21
led4Pin = 25
Z_Pin = 12

def analogRead(chn):
    bus.write_byte(address,cmd+chn)
    value = bus.read_byte(address)
    value = bus.read_byte(address)
    return value

def analogWrite(value):
    bus.write_byte_data(address,cmd,value)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setmode(GPIO.HIGH)
    GPIO.setup(Z_Pin,GPIO.IN,GPIO.PUD_UP)

def loop():
    while True:
        val_Z = GPIO.input(Z_Pin)
        val_Y = analogRead(0)
        val_X = analogRead(1)

        print("value_X:%d,\tvalue_Y:%d,\tvalue_Z:%d"%(val_X,val_Y, val_Z))
        time.sleep(0.01)

def ledfunc(val_Y):
    if val_Y > 205: 
        GPIO.setmode(ledPin, GPIO.HIGH)
    else:
        GPIO.setmode(GPIO.LOW)        
    
def led2func(val_Y):
    if val_Y < 50:
        GPIO.setmode(led2Pin, GPIO.HIGH)
    else:
        GPIO.setmode(led2Pin, GPIO.LOW)

def led3func(val_X):
    if val_X > 205: 
        GPIO.setmode(led3Pin, GPIO.HIGH)
    else:
        GPIO.setmode(GPIO.LOW)        

def led4func(val_X):
    if val_X < 50: 
        GPIO.setmode(led4Pin, GPIO.HIGH)
    else:
        GPIO.setmode(GPIO.LOW)     

def destroy():
    bus.close()
    GPIO.cleanup()

if __name__ =='__main__':
    print('Program is starting...')
    setup()
    ledfunc()
    led2func()
    led3func()
    led4func()
    try:
        loop()

    except KeyboardInterrupt:
        destroy()