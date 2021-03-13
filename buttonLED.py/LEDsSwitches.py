import RPi.GPIO as GPIO
ledPin = 11
led2Pin = 13
buttonPin = 12
button2Pin = 16

def setup():
    print('program is starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(led2Pin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW:
            GPIO.output(ledPin, GPIO.HIGH)
            print ('led on...')
        elif GPIO.input(button2Pin)==GPIO.LOW:
            GPIO.output(led2Pin, GPIO.HIGH)
            print ('led on...')
        else:
            GPIO.output(ledPin,GPIO.LOW)
            print ('led off')
            GPIO.output(led2Pin,GPIO.LOW)
            print ('led off')

def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.output(led2Pin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()