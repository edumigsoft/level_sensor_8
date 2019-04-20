#
#
#
import mfrc522
from os import uname

class RFID:
    
    def __init__(self):
        #Provoca rst usando 0,2
        #possivelmente precisa esperar um tempo para poder usar estes pinos
        #pois fazem parte do boot
        #rfid = mfrc522.MFRC522(0, 2, 4, 5, 14)
        #                           sck, mosi, miso, rst, cs(sda)
        #                           D6   D7    D2    D1   D5      
        self.rfid = mfrc522.MFRC522(12, 13, 4, 5, 14)
    
    def read(self):
        #print("read()")
        tag_type = ""
        raw_uid = ""
        uid = ""
        flag = True
        while (flag):#True):
            print("")
            print("Place card before reader to read from address 0x08")
            print("")

            try:
                (stat, tag_type) = self.rfid.request(self.rfid.REQIDL)
        
                if stat == self.rfid.OK:
                    (stat, raw_uid) = self.rfid.anticoll()
                    print("New card detected")
                    print("  - tag type: 0x%02x" % tag_type)
                    print("  - raw_uid: " + str(raw_uid))
                    uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                    print("  - uid: " + uid)
                    print("")
                    flag = False
                    #return (tag_type, raw_uid, uid)
                    
            except KeyboardInterrupt:
                print("Bye")
                flag = false
                #return (False, 0, 0)
                
        return (tag_type, raw_uid, uid)        
########################################################################
