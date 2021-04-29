from bt import get_scan_data, run_scan
from typing import Optional
from fastapi import FastAPI, Request
from empldb import DB
import uvicorn
from cryptography.fernet import Fernet
import base64
from pydantic import BaseModel


# acts as a DTO
# class RaspiReq(BaseModel):
#     adr: str
#     empName: str
#     deviceID: str


# i guess this is going to be hard coded on the clients...
# in production you wouldn't want to do this but w/e
'''
ideally this would be in a file that is fetched at startup by the
clients to allow for occasional key rotations.

We could emulate this easily
'''
serverKey = "0THr7WoWWlQssGPt08HeKg-5mXm_hUaR3zeqfLVXQ5Q="
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test/{content}")
def test(content):
    fernet = Fernet(serverKey)
    decMess = fernet.decrypt(str.encode(content)).decode()
    return {"response": decMess}


@app.post("/jsontest/")
def test(req):
    fernet = Fernet(serverKey)
    decMess = fernet.decrypt(str.encode(req.adr)).decode()
    return {"response": decMess}


@app.post("")
def verify():
    return {"IsAuth": True}


if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port="8000")
    myDB = DB()
    myDB.add_records(get_scan_data(2))
    myDB.close()
