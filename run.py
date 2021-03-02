import sqlite3
from cryptography.fernet import Fernet 

# conn = sqlite3.connect('test.db')
# curs = conn.cursor()
# # the db needs: bt adr, employee name, device id
# curs.execute("""CREATE TABLE IF NOT EXISTS auth(adr TEXT, empName TEXT, devID INTEGER)""")
# conn.commit()

# print('DONE')

print(Fernet.generate_key())