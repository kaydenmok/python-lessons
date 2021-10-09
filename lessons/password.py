import RPi.GPIO as GPIO
import Keypad
ROWS = 4
COLS = 4
keys = ['1','2','3','A','4','5','6','B','7','8','9','C','*','0','#','D']
password = ['1', '2', '3']
rowsPins = [12, 16,18,22]
colsPins = [19,15,13,11]
ledPins = [36, 38, 40]   #36 (16)= red, 38 (20) = green, 40 (21) = yellow
def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)
    for pin in ledPins:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)


def loop():
    keypad = Keypad.Keypad(keys,rowsPins,colsPins, ROWS,COLS)
    keypad.setDebounceTime(50)
    keysList = []
    status = False
    while(True):
        key = keypad.getKey()
        if(key != keypad.NULL):
            if(key == 'D'):
            # If the key is D then check password and reset the list
                if (checkPassword(keysList)):
                    print('Pass')
                    status = True
                    GPIO.output(ledPins[1], GPIO.HIGH)
                    GPIO.output(ledPins[0], GPIO.LOW)
                    GPIO.output(ledPins[2], GPIO.LOW)
                else:
                    status = False
                    print('Wrong password')
                    GPIO.output(ledPins[0], GPIO.HIGH)
                    GPIO.output(ledPins[1], GPIO.LOW)
                    GPIO.output(ledPins[2], GPIO.LOW)
                    
                keysList = []
            elif(key == 'A' and status == True):
                GPIO.output(ledPins[0], GPIO.LOW)
                GPIO.output(ledPins[1], GPIO.LOW)
                GPIO.output(ledPins[2], GPIO.HIGH)
                password = updatePassword(keypad)
                print(f"password updated: {password}")
            else:
                # Else add to the list
                print("You Pressed Key : %c "%(key))
                keysList.append(key)

# Input: typed password from user
# Doing: Matching the passwords
# Output: return true or false
def checkPassword(keyPress):

    matches = [i for i, j in zip(password, keyPress) if i == j]
    print(matches)
    if len(matches) == len(password) == len(keyPress):
        return True
    else:
        return False
        
def updatePassword(keypad):
    newPassword = []

    # The loop to catch all the typed keypad until enter
    while(True):
        key = keypad.getKey()
        if(key != keypad.NULL):
            if(key == 'D'):
                break
            else:
                newPassword.append(key)
    # return new password
    return newPassword

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()



# Type right password + enter => Green LED is on, otherwise Red LED is on
# Add new password/Reset password if the green LED is on (not Red LED)