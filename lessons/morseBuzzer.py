# Write your code here :-)
import RPi.GPIO as GPIO
import time
buzzerPin = 11
buttonPin = 12
def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT)
    GPIO.setup(buttonPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buzzerOn(seconds = 1):

    GPIO.output(buzzerPin, GPIO.HIGH)

    time.sleep(seconds)

    GPIO.output(buzzerPin, GPIO.LOW)

    time.sleep(seconds)

def loop():
    count = 0
    while count < 2:
        print(count)

        #k
        buzzerOn(3)

        buzzerOn(1)

        buzzerOn(3)
        #a
        buzzerOn(1)

        buzzerOn(3)
        #y
        buzzerOn(3)

        buzzerOn(1)

        buzzerOn(3)

        buzzerOn(3)
        #d
        buzzerOn(3)

        buzzerOn(1)

        buzzerOn(1)
        #e
        buzzerOn(1)
        #n
        buzzerOn(3)

        buzzerOn(1)

        count = count + 1


def destroy():

    GPIO.output(buzzerPin, GPIO.LOW)

    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()