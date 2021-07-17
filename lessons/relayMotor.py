import RPi.GPIO as GPIO
import time

relayPin = 11
buttonPin = 12

def setup():
    print("Initialization")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relayPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN)

def loop():
    i = 0
    g = 0
    while True:
        reading = GPIO.input(buttonPin)
        # if reading == GPIO.HIGH & g==0:
        time.sleep(0.3)
            # reading = GPIO.input(buttonPin)
        if reading == GPIO.HIGH:
            #     i = i + 1
            #     i = i % 2
            #     g = 1
            #     if i==0:
            #     if i==1:
            GPIO.output(relayPin, GPIO.HIGH)
            print('relayPin...On')
        else:
            # g=0
            GPIO.output(relayPin, GPIO.LOW)
            print("relayPin... off")

def destroy():
    GPIO.output(relayPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ =="__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

