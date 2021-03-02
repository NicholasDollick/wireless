from typing import Optional
from fastapi import FastAPI, Request
import sqlite3
import uvicorn
from cryptography.fernet import Fernet 
import base64

# filthy global vars
app = FastAPI()
conn = sqlite3.connect('test.db')
curs = conn.cursor()

serverKey = "0THr7WoWWlQssGPt08HeKg-5mXm_hUaR3zeqfLVXQ5Q="


@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/sum/")
# def sum(numA: int, numB: int):
#     return {"sum": numA + numB}

@app.get("/test/{content}")
def test(content: str):
    fernet = Fernet(serverKey)
    decMess = fernet.decrypt(str.encode(content)).decode()
    return {"response": decMess}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=222)