import RPi.GPIO as GPIO
import time
import random
pins = {'pinR':11,'pinG':12,'pinB':13}
def setup():
    global pR,pG,pB
    print ("Progam is starting...")
    GPIO.setmode(GPIO.BOARD)
    for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], GPIO.HIGH)
    pR = GPIO.PWM(pins['pinR'],1)
    pG = GPIO.PWM(pins['pinG'],1)
    pB = GPIO.PWM(pins['pinB'],1)
    pR.start(0)
    pG.start(0)
    pB.start(0)
def setColor(rVal,gVal,bVal):
    pR.ChangeDutyCycle(rVal)
    pG.ChangeDutyCycle(gVal)
    pB.ChangeDutyCycle(bVal)

def loop():
    while True:
        r=random.randint(0,100)
        g=random.randint(0,100)
        b=random.randint(0,100)
        setColor(r,g,b)
        print ('r=%d, g=%d, b=%d' %(r,g,b))
        time.sleep(0.7)

def destroy():
    pR.stop()
    pG.stop()
    pB.stop()
    GPIO.cleanup()
if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()
