import sqlite3

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
                        MAC text,
                        IsEmployee Int
                        )
        """)


    def add_records(self,tList):
        conn = self.conn
        db = self.db
        with conn:
            for addr, name in tList:
                db.execute("""
                INSERT OR IGNORE INTO employeesBT(DeviceName,MAC)
                VALUES(?,?)
                """,
                (name, addr))



    def set_employee(self,first,last,mac):
        conn = self.conn
        db = self.db
        with conn:
            db.execute("""
            UPDATE employeesBT
            SET FirstName = ?, LastName  = ?
            WHERE MAC = ?
            """,first,last,mac)


    def close(self):
        self.conn.close()
