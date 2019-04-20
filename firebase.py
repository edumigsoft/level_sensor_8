#
# -*- coding: utf-8 -*-
#
import const
import connect
import network
import json

try:
    import urequests as requests
except:
    import requests

try:
    import usocket as _socket
except:
    import _socket

try:
    import ussl as ssl
except:
    import ssl

class FIREBASE:
    
    def __init__(self):
        
        pass

    def get(self, key = "", subkey = ""):
        
        if (connect.do_connect()):
            
            print("Firebase")
            URL = const.FIREBASE_HOST + "/"

            if len(key) > 0:
                URL += key #+ "/"
                if len(subkey) > 0:
                    URL += "/" + subkey
                
            URL += ".json"
                    
            print(URL)
                
            try:
                response = requests.get(URL)
                print(response.status_code)
                #print(response.text)
                print("\r\n")
                text = response.text
                #response.close()
                return text
            except:
                print("ERROR!!!")


    def set(self, key, value):
        
        if (connect.do_connect()):
            
            print("Firebase")
            URL = const.FIREBASE_HOST + "/"

            URL += ".json"
                    
            print(URL)            

            data = {key:value}
            response = requests.patch(URL, data=json.dumps(data))
            print(response.status_code)
            text = response.text
            #response.close()
            #print(.text)
            print("\r\n")
            
            return text

########################################################################
