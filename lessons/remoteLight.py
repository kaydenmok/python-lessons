import RPi.GPIO as GPIO
import time
PIN = 26
ledPins = [11,12,13,15,16]


def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN,GPIO.IN,GPIO.PUD_UP)
    for pin in ledPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)


# Execute the command
def exec_cmd(key_val):
    if(key_val==0x45):
        turnOn()
    elif(key_val==0x46):
        flowLeft2Right()
    elif(key_val==0x47):
        flowRight2Left()
    else:
        turnOff()
#commands------------------------

def turnOff():
    for pin in ledPins:
        GPIO.output(pin, GPIO.LOW)   

def flowLeft2Right():
    for pin in ledPins:
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(pin, GPIO.LOW)

def flowRight2Left():
    for pin in ledPins[::-1]:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(pin, GPIO.LOW) 
    
def turnOn():
    for pin in ledPins:
        GPIO.output(pin, GPIO.HIGH)
#----------------------------------------------

def loop():
    while True:
        if GPIO.input(PIN) == 0:
            count = 0
            while GPIO.input(PIN) == 0 and count < 200:
                count += 1
                time.sleep(0.00006)

            count = 0 
            while GPIO.input(PIN) == 1 and count < 80:
                count += 1
                time.sleep(0.00006)

            idx = 0
            cnt = 0
            data = [0,0,0,0]
            for i in range(0,32):
            
                count = 0 
                while GPIO.input(PIN) == 0 and count < 15:
                    count += 1
                    time.sleep(0.00006)

                count = 0 
                while GPIO.input(PIN) == 1 and count < 40:
                    count += 1
                    time.sleep(0.00006)

                if count > 8:
                    data[idx] |= 1<<cnt
                if cnt == 7:
                    cnt = 0
                    idx += 1 
                else:
                    cnt += 1
            if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:
                print("Get the key: 0x%02x" %data[2])
                exec_cmd(data[2])

def destroy():
    GPIO.output(PIN, GPIO.LOW)
    GPIO.cleanup()

if __name__ =='__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        