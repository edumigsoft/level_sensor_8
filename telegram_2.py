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

#import firebase

def getMessages(messages):
    
    if (connect.do_connect()):

        s = _socket.socket()
    
        ai = _socket.getaddrinfo(const.TELEGRAM_API, const.TELEGRAM_PORT)
        #print("Address infos:", ai)
        addr = ai[0][-1]

        print("Connect address Telegram:", addr)
        s.connect(addr)
    
        s.settimeout(const.TELEGRAM_TIMEOUT)
    
        s = ssl.wrap_socket(s)
        #print(s)
        print("\r\n")

        getRequest = "GET /bot"
        getRequest += const.TELEGRAM_TOKEN
        getRequest += messages
        getRequest += " HTTP/1.0\r\n\r\n"

        s.write(getRequest)
        quote = s.read(4096)
        #print(quote)
        quote = quote.decode("ascii")
        #print(quote)
        #print("\r\n")
        if (len(quote) > 0):
            #print(quote)
            
            ind = quote.find("\r\n\r\n")
            quote = quote[ind:]
            quote = json.loads(quote)
            try:
                quote = quote["result"][0]
            except:
                quote = quote["result"]
        else:
            quote = "No Message"

        #print("\r\n")
        s.close()
        
        return quote
#####################################################################

update_id = 0

def getUpdates():
    
    global update_id
    
    #if update_id == 0:
    #    update_id = int(firebase.get(const.FIREBASE_LAST_MESSAGE))
    
    updates = "/getUpdates";
    updates += "?";
    updates += "&limit=" + str(1);
    #updates += "&timeout=" + str(100);
    updates += "&offset=" + str(update_id);
    
    print("getUpdates")
    
    URL = const.TELEGRAM_URL + updates
    response = requests.get(URL)
    #print(response.status_code)
    #print(response.text)
    
    messages = json.loads(response.text)
    try:
        messages = messages["result"][0]
    except:
        messages = messages["result"]

    if "update_id" in messages:
        up_id2 = int(str(messages["update_id"]))
        #print("up_id2 = " + str(up_id2))
        if (update_id <= up_id2):
            update_id = up_id2 + 1
            #print("up_id2 + 1 = " + str(update_id))
            #firebase.set(const.FIREBASE_LAST_MESSAGE, update_id)

    #print(messages)
    print("\r\n")
    
    return messages
#####################################################################

def getMe():
    
    updates = "/getMe";
    
    print("getMe")
    URL = const.TELEGRAM_URL + updates
    response = requests.get(URL)
    #print(response.status_code)
    #print(response.text)
    print("\r\n")
        
    messages = json.loads(response.text)
    messages = messages["result"]
    
    return messages
#####################################################################

def sendMessage(chat_id, message):
    
    if chat_id == 0:
        return ""

    if len(message) == 0:
        return ""

    message = message.strip().replace(" ", "%20")
    message = "?chat_id=" + str(chat_id) + "&text=" + message
    URL = const.TELEGRAM_URL
    URL += "/sendMessage"
    URL += message
    
    print(URL)
    
    data = requests.post(URL)
    print(data)
    print("\r\n")
#####################################################################
