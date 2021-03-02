# this is the file that is going to make the api call
import requests
import base64
from cryptography.fernet import Fernet 

serverKey = "0THr7WoWWlQssGPt08HeKg-5mXm_hUaR3zeqfLVXQ5Q="

url = "http://127.0.0.1:222/test/"

#params = {'test':"hello server"}
content = "this is the message I want to see on the server"

fernet = Fernet(serverKey)
encMess = fernet.encrypt(content.encode())


r = requests.get(url+encMess)
data = r.json()
print(data)