import RPi.GPIO as GPIO
import mfrc522
import sys
import os

#create an object of the class MFRC522
mfrc = mfrc522.MFRC522()
def dis_CommandLine():
    print("RC522>", end="")
def dis_CardID(cardID):
    print("%2X%2X%2X%2X%2X>"%(cardID[0],cardID[1],cardID[2],cardID[3],cardID[4]),end="")

def setup():
    print("Program is starting...")
    print("Press Ctrl-C to exit")
    pass

def loop():
    global mfrc
    while(True):
        dis_CommandLine()
        inCmd = input()
        print(inCmd)
        if (inCmd == "scan"):
            print ("Scanning...")
            mfrc = mfrc522.MFRC522()
            isScan = True
            while isScan:
                #SCAN FOR CARDS
                (status, TagType) = mfrc.MFRC522_Request(mfrc.PICC_REQIDL)
                #If a card is found
                if status == mfrc.MI_OK:
                    print("Card detected")
                #Get the uid of the card
                (status,uid) = mfrc.MFRC522_Anticoll()
                #If we have the UID, continue
                if status == mfrc.MI_OK:
                    print ("Card UID: "+str(map(hex,uid)))
                    #Select the scanned tag
                    if mfrc.MFRC522_SelectTag(uid) == 0:
                        print("MFRC522_SelectTag Failed!")
                    if cmdloop(uid) < 1:
                        isScan = False

        elif inCmd == "quit":
            destroy()
            exit()
        else:
            print("\tUnknown command\n"+"\tscan:scan card and dump\n"+"\tquit:exit program\n")

def cmdloop(cardID):
    pass
    while(True):
        dis_CommandLine()
        dis_CardID(cardID)
        inCmd = input()
        cmd = inCmd.split("")
        print(cmd)
        if(cmd[0] == "read"):
            blockAddr = int(cmd[1])
            if((blockAddr<0) or (blockAddr>63)):
                print("Invalid Access")
            #This is the default key for authentication
            key = [0xFF,0XFF,0XFF,0XFF,0XFF,0XFF]
            #autheniticate
            status = mfrc.MFRC522_Auth(mfrc.PICC_AUTHENTIA, blockAddr, key, cardID)
            #Check if autheniticated
            if status == mfrc.MI.OK:
                mfrc.MFRC522_Readstr(blockAddr)
            else:
                print("Authentication error")
                return 0

                    
        elif cmd[0] == "dump":
            #This is the default key for authentication
            key = [0xFF,0XFF,0XFF,0XFF,0XFF,0XFF]
            mfrc.MFRC522_Dump_Str(key,cardID)

        elif cmd[0]== "write":
            blockAddr = int(cmd[1])
            if((blockAddr<0) or (blockAddr>63)):
                print("Invalid Address!")
            data = [0]*16
            if(len(cmd)<2):
                data = [0]*16
            else:
                data = cmd[2][0:17]
                data = map(ord,data)
                data = list(data)
                lenData = len(list(data))
                if lenData<16:
                    data+=[0]*(16-lenData)
            #This is the default key for authentication
            key = [0xFF,0XFF,0XFF,0XFF,0XFF,0XFF]
            #Authenticate

            status = mfrc.MFRC522_Auth(mfrc.PICC_AUTHENTIA, blockAddr, key, cardID)
            #Check if authenticated
            if status == mfrc.MI_OK:
                print ("Before writing,. the data in block %d is: "%(blockAddr))
                mfrc.MFRC522_Readstr(blockAddr)
                mfrc.MFRC522_Write(blockAddr, data)
                print("After written, The data in block %d is: "%(blockAddr))
                mfrc.MFRC522_Readstr(blockAddr)
            else:
                print("Authenitcation error")
                return 0

        elif cmd[0] == "clean":
            blockAddr=int(cmd[1])
            if((blockAddr<0) or (blockAddr>63)):
                print("Invalid Address")
            data = [0]*16
            #This is the default key for authentication
            key = [0xFF,0XFF,0XFF,0XFF,0XFF,0XFF]
            #Authenicate
            status = mfrc.MFRC522_Auth(mfrc.PICC_AUTHENTIA, blockAddr, key, cardID)
            #Check if authenticated
            if status == mfrc.MI_OK:
                print ("Before cleaning , the data in block %d is:"%(blockAddr))
                mfrc.MFRC522_Readstr(blockAddr)
                mfrc.MFRC522_Write(blockAddr, data)
                print("After cleaned, the data in block %d is:"%(blockAddr))
                mfrc.MFRC522_Readstr(blockAddr)
            else:
                print("Authentication error")
                return 0
        elif cmd[0] == "halt":
            return 0
        else:
            print("Usage:\r\n""\tread<blcokstart>\r\n""\tdump\r\n""\thalt\r\n""\tclean<blcokaddr>\r\n""\twrite<blockaddr><data>\r\n")
def destroy():
    GPIO.cleanup()

if __name__ =='__main__':
    setup()
    try:
        loop()

    except KeyboardInterrupt:
        destroy()               
