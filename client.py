# this is the file that is going to make the api call
import requests
import base64
from cryptography.fernet import Fernet 

serverKey = "0THr7WoWWlQssGPt08HeKg-5mXm_hUaR3zeqfLVXQ5Q="

url = "http://127.0.0.1:222/jsontest/"

#params = {'test':"hello server"}


# poll for bluetooth devices

# this would be the device address
content = "this is the message I want to see on the server"


fernet = Fernet(serverKey)
encMess = fernet.encrypt(content.encode())

# in theory this entire thing could be encrypted if we wanted to
params = {"adr": str(encMess),
          "empName": "Testy",
          "deviceID": "222"
         }

print(params)
print()
r = requests.post(url, json=params)
data = r.json()
print(data)