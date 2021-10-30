import RPi.GPIO as GPIO

ledPin = 12
sensorPin = 11

def setup():
    print('starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(sensorPin, GPIO.IN)

def loop():
    while True:
        if GPIO.input(sensorPin)==GPIO.HIGH:
            GPIO.output(ledPin, GPIO.HIGH)
            print(GPIO.input(sensorPin))
            print('led on...')

        else:
            GPIO.output(ledPin, GPIO.LOW)
            print('led off...')

def destroy():
    GPIO.cleanup()
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        
