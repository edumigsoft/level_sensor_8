#
#
#
#import const
#import rfid_read as rfid
#import firebase
#import telegram
#import json
import time
from machine import I2C, Pin

class APP:
    
    def __init__(self):
        
        #self.rfid = rfid.RFID()
        #self.firebase = firebase.FIREBASE()
        #self.telegram = telegram.TELEGRAM()
        pass

    def main(self):
        
        print("APP main")
        
        i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
        
        #while True:
        #    print("Scan")
        #    print(i2c.scan())
        #    time.sleep(2)

        #print("Scan")
        #print(i2c.scan())
        #addr = i2c.scan()[0]
        #print(addr)
        addr = 8
        #time.sleep(1)

        #print("Read...")
        #print(i2c.readfrom(addr, 15))
        #time.sleep(1)
        
        while True:
            print("Read...")
            uid = i2c.readfrom(addr, 9)
            print(uid)
            if "3a424d43" in uid:
                i2c.writeto(addr, "10")            
            time.sleep(1)
        
        #print("Write...")
        #i2c.writeto(addr, "Hello, by NodeMCU!!")

        #buf = bytearray(10)     # create a buffer with 10 bytes
        #i2c.writeto(0x2, buf)  # write the given buffer to the slave


#    def main2(self):

#        print("APP main")
#        print("\r\n")

#        uid_rfid = self.rfid.read()
#        uid = str(uid_rfid[2])

#        if len(uid) > 0:

#            print(uid)
#            print("\r\n")
#            time.sleep(2)

            #read_firebase = self.firebase_get()
            #uid = "0x4ab0b77a"
#            read_firebase = self.firebase.get(const.FIREBASE_USERS, uid)
#            print(read_firebase)
#            print("\r\n")
#            time.sleep(1)

#            read_telegram = self.telegram.sendMessage(179952633, uid)
#            #read_telegram = self.telegram.sendMessage(179952633, read_firebase)
#            print(read_telegram)
#            print("\r\n")
#            time.sleep(1)
            
#            update_id = int(self.firebase.get(const.FIREBASE_LAST_MESSAGE))
#            print(update_id)
#            print("\r\n")
#            read_telegram = self.telegram.getUpdates(update_id)
#            print(read_telegram)
#            print("\r\n")
#            if "update_id" in read_telegram:
#                up_id2 = int(read_telegram["update_id"])
#                if (update_id <= up_id2):
#                    update_id = up_id2 + 1
                    #print("up_id2 + 1 = " + str(update_id))
#                    read_firebase = self.firebase.set(const.FIREBASE_LAST_MESSAGE, update_id)
#                    print(read_firebase)
#                    print("\r\n")

            #read_firebase = self.firebase.set(const.FIREBASE_LED_STATUS, 1)
            #print(read_firebase)
            #print("\r\n")
            
#        else:
#            print("ERROR READ TAG!!")

########################################################################
