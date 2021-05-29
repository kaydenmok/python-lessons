import RPi.GPIO as GPIO
import smbus
import time
import math
address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40
def analogRead(chn):
    value = bus.read_byte_data(address,cmd+chn)
    return value

def analogWrite(value):
    bus.write_byte_data(address,cmd,value)

def setup():
    GPIO.setmode(GPIO.BOARD)

def loop():
    while True:
        value = analogRead(0)
        voltage = value / 255.0 * 3.3
        Rt = 10 * voltage / (3.4 - voltage)
        tempK = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0)
        tempC = tempK - 273.15
        print("ADC Value : %d, Voltage : %.2f, Temperature : %.2f"%(value, voltage, tempC))
        time.sleep(0.01)

def destroy():
    GPIO.cleanup()
if __name__ == "__main__":
    print("Program is starting")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()