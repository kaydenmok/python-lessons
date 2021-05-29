import RPi.GPIO as GPIO
import smbus
import time
#j
address = 0x48
bus=smbus.SMBus(1)
cmd=0x40
ledPin = 22
led2Pin = 24
led3Pin = 29
led4Pin = 6
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
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(led2Pin, GPIO.OUT)
    GPIO.setup(led3Pin, GPIO.OUT)
    GPIO.setup(led4Pin, GPIO.OUT)


def loop():
    while True:
        val_Z = GPIO.input(Z_Pin)
        val_Y = analogRead(0)
        val_X = analogRead(1)

        ledFunc(val_X, val_Y, val_Z)

        print("value_X:%d,\tvalue_Y:%d,\tvalue_Z:%d"%(val_X,val_Y, val_Z))
        time.sleep(0.01)


def ledFunc(val_X, val_Y, val_Z):
    if val_Y > 205: 
        ledSwitch(ledPin, True)
    else:
        ledSwitch(ledPin, False)

    if val_Y < 50:
        ledSwitch(led2Pin, True)
    else:
        ledSwitch(led2Pin, False)

    if val_X > 205: 
        ledSwitch(led3Pin, True)
    else:
        ledSwitch(led3Pin, False)

    if val_X < 50: 
        ledSwitch(led4Pin, True)
    else:
        ledSwitch(led4Pin, False)    

def ledSwitch(ledPin, isOn = False):
    GPIO.setmode(ledPin, GPIO.HIGH if isOn else GPIO.LOW)


def destroy():
    bus.close()
    GPIO.cleanup()

if __name__ =='__main__':
    print('Program is starting...')
    setup()
    try:
        loop()

    except KeyboardInterrupt:
        destroy()