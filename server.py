from bt import get_scan_data, run_scan
from typing import Optional
from empldb import DB
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

if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port="8000")
    myDB = DB()
    myDB.add_records(get_scan_data(2))
    #empl = ("Manuel","Loera","mloera7290@sdsu.edu","Manuel's iPhone 12")  <<<< example tuple for setemployee
    #myDB.set_employee(empl)
    myDB.close()
