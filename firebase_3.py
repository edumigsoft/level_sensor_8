#
#
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

    def get(self, Key = ""):
    
        if (connect.do_connect()):
            
            print("Firebase")
            URL = const.FIREBASE_HOST
            if len(Key) > 0:
                URL += "/" + Key
            #print(URL)
            
            #URL = self.parseURL(URL)
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
            
            response = requests.get(URL)
            #print(response.status_code)
            #print(response.text)
            print("\r\n")
            
            return response.text

    def set(Key, Value):
        
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

            data = {Key:Value}
            response = requests.patch(URL, data=json.dumps(data))
            #print(response.status_code)
            #print(response.text)
            print("\r\n")
            
            return response.text

    def parseURL(self, url):
        
        if '.firebaseio.com' not in url.lower():
            if '.json' == url[-5:]:
                url = url[:-5]
            if '/' in url:
                if '/' == url[-1]:
                    url = url[:-1]
                url = 'https://' + \
                    url.split('/')[0] + '.firebaseio.com/' + url.split('/', 1)[1] + '.json'
            else:
                url = 'https://' + url + '.firebaseio.com/.json'
            return URL

        if 'http://' in url:
            url = url.replace('http://', 'https://')
        if 'https://' not in url:
            url = 'https://' + url
        if '.json' not in url.lower():
            if '/' != url[-1]:
                url = url + '/.json'
            else:
                url = url + '.json'

########################################################################
