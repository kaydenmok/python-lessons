import RPi.GPIO as GPIO
import smbus
import time
#j
address = 0x48
bus=smbus.SMBus(1)
cmd=0x40
ledWhitePin = 31
ledGreenPin = 18
ledRedPin = 40
ledBluePin = 15
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
    GPIO.setup(Z_Pin,GPIO.IN,GPIO.PUD_UP)
    GPIO.setup(ledWhitePin, GPIO.OUT)
    GPIO.output(ledWhitePin, GPIO.LOW)
    GPIO.setup(ledGreenPin, GPIO.OUT)
    GPIO.output(ledGreenPin, GPIO.LOW)
    GPIO.setup(ledRedPin, GPIO.OUT)
    GPIO.output(ledRedPin, GPIO.LOW)
    GPIO.setup(ledBluePin, GPIO.OUT)
    GPIO.output(ledBluePin, GPIO.LOW)


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
        ledSwitch(ledWhitePin, True)
    else:
        ledSwitch(ledWhitePin, False)

    if val_Y < 50:
        ledSwitch(ledGreenPin, True)
    else:
        ledSwitch(ledGreenPin, False)

    if val_X > 205: 
        ledSwitch(ledRedPin, True)
    else:
        ledSwitch(ledRedPin, False)

    if val_X < 50: 
        ledSwitch(ledBluePin, True)
    else:
        ledSwitch(ledBluePin, False)    

def ledSwitch(ledWhitePin, isOn = True):
    GPIO.output(ledWhitePin, GPIO.HIGH if isOn else GPIO.LOW)


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