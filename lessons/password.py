import RPi.GPIO as GPIO
import Keypad
ROWS = 4
COLS = 4
keys = ['1','2','3','A','4','5','6','B','7','8','9','C','*','0','#','D']

rowsPins = [12, 16,18,22]
colsPins = [19,15,13,11]
ledPins = [36, 38]   #36 (16)= red, 38 (20) = green
def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    for pin in ledPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)


def loop():
    keypad = Keypad.Keypad(keys,rowsPins,colsPins, ROWS,COLS)
    keypad.setDebounceTime(50)
    keysList = []
    while(True):
        key = keypad.getKey()
        if(key != keypad.NULL):
            if(key == 'D'):
            # If the key is D then check password and reset the list
                if (checkPassword(keysList)):
                    print('Pass')
                    GPIO.output(ledPins[1], GPIO.LOW)
                    GPIO.output(ledPins[0], GPIO.HIGH)
                else:
                    print('Wrong password')
                    GPIO.output(ledPins[0], GPIO.LOW)
                    GPIO.output(ledPins[1], GPIO.HIGH)
                    
                keysList = []
            else:
                # Else add to the list
                print("You Pressed Key : %c "%(key))
                keysList.append(key)

# Input: typed password from user
# Doing: Matching the passwords
# Output: return true or false
def checkPassword(keyPress):
    password = ['1', '2', '3']
    matches = [i for i, j in zip(password, keyPress) if i == j]
    print(matches)
    if len(matches) == len(password):
        return True
    else:
        return False
        
    


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()



# Type right password + enter => Green LED is on, otherwise Red LED is on
# Add new password/Reset password if the green LED is on (not Red LED)