import RPi.GPIO as GPIO
import time
PIN = 26
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN,GPIO.IN,GPIO.PUD_UP)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    print("irm test start.......................")

def exec_cmd(key_val):
    if(key_val==0x45):
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
    elif(key_val==0x46):
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
    elif(key_val==0x47):
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(27, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)

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
        

