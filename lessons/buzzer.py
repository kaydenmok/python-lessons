import RPi.GPIO as GPIO
buzzerPin = 11
buttonPin = 12
def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT)
    GPIO.setup(buttonPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW:
            GPIO.output(buzzerPin,GPIO.HIGH)
            print ('buzzer on')
        else:
            GPIO.output(buzzerPin,GPIO.LOW)
            print('buzzer off')
def destroy():
    GPIO.output(buzzerPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
