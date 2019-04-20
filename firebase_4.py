#
# -*- coding: utf-8 -*-
#
#Example
#users = '{"users": {"0x4ab0b77a": {"admin":"True", "credit_200":-1, "credit_300":-1}, "0x067e3103": {"admin":"False", "credit_200":5, "credit_300":4}}}'
#users = json.loads(users)
#read_firebase = firebase.set(users)
#print(read_firebase)
# No momento o get não funciona para este tipo de json, gera exceção

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

def get(key = "", subkey = ""):
    
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
            response.close()
            return text
        except:
            print("ERROR!!!")
#####################################################################

def set(data):
    if (connect.do_connect()):
        
        print("Firebase")
        URL = const.FIREBASE_HOST
        
        if '.firebaseio.com' not in URL.lower():
            if '.json' == URL[-5:]:
                URL = URL[:-5]
            if '/' in URL:
                if '/' == URL[-1]:
                    URL = URL[:-1]
                URL = 'https://' + \
                      URL.split('/')[0] + '.firebaseio.com/' + URL.split('/', 1)[1] + '.json'
            else:
                URL = 'https://' + URL + '.firebaseio.com/.json'
            return URL

        if 'http://' in URL:
            URL = URL.replace('http://', 'https://')
        if 'https://' not in URL:
            URL = 'https://' + URL
        if '.json' not in URL.lower():
            if '/' != URL[-1]:
                URL = URL + '/.json'
            else:
                URL = URL + '.json'

        print(URL)
        
        try:
            response = requests.patch(URL, data=json.dumps(data))
            print(response.status_code)
            #print(response.text)
            print("\r\n")
            return response.text
        except:
            print("ERROR!!!")
#####################################################################
