import sqlite3
import datetime

# DB class contains functions to interact with sqlite db for CRUD ops. Default creates a db with necessarry columns for our db
class DB:
    conn = sqlite3.connect('employeesBT.db')
    db = conn.cursor()
    with conn:
        db.execute("""
        CREATE TABLE IF NOT EXISTS employeesBT (
                        id integer PRIMARY KEY,
                        FirstName text,
                        LastName text,
                        DeviceName text,
                        MAC text UNIQUE,
                        Email text,
                        LastTimeScan,
                        ClockIn text,
                        ClockOut text,
                        IsEmployee Int
                        )
        """)

    # takes in list of tuples from run scan that contains a list of addr(mac),name tuples and inserts into db
    def add_records(self,tList):
        conn = self.conn
        db = self.db
        with conn:
            for addr, name in tList:
                db.execute("""
                INSERT OR IGNORE INTO employeesBT(DeviceName,MAC,LastTimeScan)
                VALUES(?,?,?)
                """,
                (name,addr,datetime.datetime.now()))


    # accepts a tuple of (firstname,lastname,email,DevName) to mutate record by DevName
    def set_employee(self,argTuple):
        first,last,email,DevName=argTuple
        conn = self.conn
        db = self.db
        with conn:
            db.execute("""
            UPDATE employeesBT
            SET FirstName = ?, LastName  = ?, Email = ?,LastTimeScan = ? ,IsEmployee = 1
            WHERE DeviceName = ?
            """,(first,last,email,datetime.datetime.now(),DevName))
            
    # accepts a tuple of (firstname,lastname,email,DevName) to mutate record by DevName
    def set_timeClockIn(self,argTuple):
        clockIn,DevName=argTuple
        conn = self.conn
        db = self.db
        with conn:
            db.execute("""
            UPDATE employeesBT
            SET ClockIn = ?
            WHERE DeviceName = ?
            """,(clockIn, DevName))
            
    # accepts a tuple of (firstname,lastname,email,DevName) to mutate record by DevName
    def set_timeClockOut(self,argTuple):
        clockOut,DevName=argTuple
        conn = self.conn
        db = self.db
        with conn:
            db.execute("""
            UPDATE employeesBT
            SET ClockOut = ?
            WHERE DeviceName = ?
            """,(clockOut, DevName))

    # accepts a mac string parameter to delete record by mac in db
    def delete_by_mac(self,mac):
        conn = self.conn
        db = self.db
        with conn:
            db.execute("""
            DELETE FROM employeesBT
            WHERE MAC = ?
            """,(mac,))

    # closes connection of DB.conn obj
    def close(self):
        self.conn.close()
