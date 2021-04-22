# this is the file that is going to make the api call
import requests
import base64
from cryptography.fernet import Fernet 
# import bluetooth

# this should be read in from a file
serverKey = "0THr7WoWWlQssGPt08HeKg-5mXm_hUaR3zeqfLVXQ5Q="

'''
cert based startup flow:
    fetch latest cert
        send device ID to server for validation
    read in from file and set serverKey
'''

url = "http://127.0.0.1:222/jsontest/"

#params = {'test':"hello server"}


# poll for bluetooth devices
'''
devices = bluetooth.discover_devices(Lookup_names=True)

# do something more usefull in this check
for addr, name in devices:
        print("adr: ", addr)
        print("name: ", name)
'''

# this would be the device address
content = "this is the message I want to see on the server"


fernet = Fernet(serverKey)
encMess = fernet.encrypt(content.encode())

# in theory this entire thing could be encrypted if we wanted to
params = {
          "TEST": "ing",
          "adr": str(encMess),
          "empName": "Testy",
          "deviceID": "222",
          "another": "one",
          "hello": "world"
         }

print(params)
print()
r = requests.post(url, json=params)
data = r.json()
print(data)