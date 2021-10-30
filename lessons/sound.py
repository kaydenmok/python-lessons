import RPi.GPIO as GPIO
import time
D0=12
LED = 11
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(D0, GPIO.IN)
    GPIO.setup(LED, GPIO.OUT)
    
def loop():
    while True:
        print('shock:')
        PIN = GPIO.input(D0)
        if PIN == GPIO.HIGH:
            GPIO.output(LED, GPIO.HIGH)
            print('LED... HIGH')
            time.sleep(1)
        else:
            GPIO.output(LED,GPIO.LOW)
            print('LED... LOW')
            time.sleep(0.3)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()