#
#
#
#import const
#import telegram
#import firebase
#import time
#import led
#import rfid_read as rfid
#
#
#

#idUser = ""

#def handleCommand(command):
    
#    command = command.lower()
#    if command == "/ledon":
#        led.ledOn()
#    elif command == "/ledoff":
#        led.ledOff()
#    elif command == "/ledtoggle":
#        led.ledToggle()
#    elif command == "/options":
#        options = "Options"#\\n/ledon\\n"
        #options += "ledon\n"
        #options += "/ledoff\n"
        #options += "/ledtoggle\n"
#        telegram.sendMessage(idUser, options)
#    else:
#        print("Invalid Command")
########################################################################

#def handleMessage(message):
    
#    global idUser
    
#    text = ""
#    type = ""
    
#    if "message" in message:
        #update_id
#        message = message["message"]
#        idUser = message["from"]["id"]
#        text = message["text"]
        #'entities': [{'offset': 0, 'length': 10, 'type': 'bot_command'}]
#        type = message["entities"][0]["type"]
    
#    if "bot_command" in type:
#        handleCommand(text)
#    else:
#        print("Message received: " + text)
#    print("\r\n")
########################################################################

def main():

    print("app main")
    
    #import blink
    
    #blk = blink.BLINK()
    #blk.blinker()
    
    
    #import rfid_read
    
    #rfid = rfid_read.RFID()
    #read = rfid.read()
    #print("read[2] (uid) = " + read[2])

    import firebase
    import const
    
    fire = firebase.FIREBASE()
    resp = fire.get(const.FIREBASE_LED_STATUS)
    print(resp)
    
    #import telegram
    
    #tel = telegram.TELEGRAM()
    #resp = tel.getMe()
    #print(resp)
    
#    led.ledExec()

    
    #while (True):
        #print(telegram.getMe())
        #print("\r\n')
        #time.sleep(5.0)
        #print(telegram.getUpdates())
        #telegram.getUpdates()
        #print("\r\n")
#        handleMessage(telegram.getUpdates())
#        time.sleep(5.0)

        #firebase.get()
        #time.sleep(5.0)
        #firebase.get(const.FIREBASE_LEDSTATUS)
        #time.sleep(5.0)
        #firebase.get(const.FIREBASE_LAST_MESSAGE)
        #time.sleep(5.0)
        #firebase.get("main")
        #time.sleep(5.0)
        
        #try:
        #    distance_cm = sensor.distance_cm()
        #    print('Distance cm:', distance_cm, 'cm')
            
        #    distance_mm = sensor.distance_mm()
        #    print('Distance mm:', distance_mm, 'mm')            
        #except OSError as ex:
        #    print('ERROR getting distance:', ex)
        
    #firebase.set(const.FIREBASE_LEDSTATUS, 1)    
    #telegram.sendMessage(179952633, "This is a message")
    #telegram.getMe()
    
    #read = False
    #while (not read):
    #    resp = rfid.read()
        #print(resp)
    #    read = resp[0]
    

########################################################################

#if __name__ == "__main__":
    #main()
