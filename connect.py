#
#
#
import const
import network
import time

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    #cont = 10
    if not sta_if.isconnected():
        print("Connecting to network")
        sta_if.active(True)
        sta_if.connect(const.WIFI_SSID, const.WIFI_PASS)
        
        while not sta_if.isconnected():
            #if cont == 0:
            #    cont = -1
            #    break;
            #cont--
            time.sleep_ms(5)
            #print('.')
    
    #if cont == -1:
        
    #print("\r\n")
    print("Network config: " + str( sta_if.ifconfig()))
    print("\r\n")

    return sta_if.isconnected()
#####################################################################
