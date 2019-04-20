#
#
#
from machine import Pin
import const
import firebase
import telegram

LED_STATUS = int(firebase.get(const.FIREBASE_LED_STATUS))
pin = Pin(const.LED_PIN, Pin.OUT, LED_STATUS)

def ledStatus_Str():
    
    if LED_STATUS == const.LED_ON:
        return "ON"
    else:
        return "OFF"
#####################################################################

def ledExec():
    
    global pin
    
    firebase.set(const.FIREBASE_LED_STATUS, int(LED_STATUS))
    pin.value(LED_STATUS)
#####################################################################

def ledOn(idUser = ""):
    
    global LED_STATUS
    
    LED_STATUS = const.LED_ON
    ledExec()
    telegram.sendMessage(idUser, "LED STATUS: " + ledStatus_Str())
    
    print("ledOn")
    print("\r\n")
#####################################################################

def ledOff(idUser = ""):
    
    global LED_STATUS
    
    LED_STATUS = const.LED_OFF
    ledExec()
    telegram.sendMessage(idUser, "LED STATUS: " + ledStatus_Str())
    
    print("ledOff")
    print("\r\n")
#####################################################################

def ledToggle(idUser = ""):
    
    global LED_STATUS
    
    if LED_STATUS == const.LED_ON:
        LED_STATUS = const.LED_OFF
    else:
        LED_STATUS = const.LED_ON
    ledExec()
    telegram.sendMessage(idUser, "LED STATUS: " + ledStatus_Str())
    
    print("ledToggle")
    print("\r\n")
#####################################################################
