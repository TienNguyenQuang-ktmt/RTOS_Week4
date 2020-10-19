import sqlite3
import random
data = sqlite3.connect("databaseOne.db")

da = data.cursor()
da.execute('''create table if not exists MOITRUONG(nhiet char[10],am char[10])''')
data = da.execute("SELECT * FROM MOITRUONG") #mssv,hoten,rtos thay the bang * de lay het
for i in data:
    print("------------*------------")
    print("NhietDO:" + str(i[0]))
    print("DOAm:" + str(i[1]))
data.close()