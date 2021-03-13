import RPi.GPIO as GPIO
import time
ledPins = [11,12,13,15,16,18,22,24]
buttonPin = 36
def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    for pin in ledPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
def loop():
    state = 0
    while True:

        if(state % 4 == 0):
            turnOff()
            print('Lights off...')
        elif(state % 4 == 1):
            flowLeft2Right()
            print ('Left 2 Right...')
        elif(state % 4 == 2):
            flowRight2Left()
            print ('Right 2 Left...')
        elif(state % 4 == 3):
            flowRight2Left()
            flowLeft2Right()
            print ('Both ways...')


        if GPIO.input(buttonPin)==GPIO.LOW:
            state += 1
            time.sleep(0.3)
            print(state)


def turnOff():
    for pin in ledPins:
        GPIO.output(pin, GPIO.HIGH)

def flowLeft2Right():
    for pin in ledPins:
            GPIO.output(pin,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)

def flowRight2Left():
    for pin in ledPins[::-1]:
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(pin, GPIO.HIGH)


def destroy():
    for pin in ledPins:
        GPIO.output(pin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()