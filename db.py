# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data

import sqlite3 as sql

#func same as runnning conn = sql.connect("test_db")

conn = sql.connect('test_db')
cursor = conn.cursor()

def setupTable():
    sql_file = open("orders.sql")
    sql_string = sql_file.read()
    cursor.executescript(sql_string)

def runQuery(query):
    data = cursor.execute(query).fetchall()
    return data

def commitChanges():
    conn.commit()


# Uncomment this and run the file once to set up the DB
#setupTable()

commitChanges()



"""    order_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    customer_name VARCHAR(30) NOT NULL,
    drink_type VARCHAR(50) NOT NULL, 
    drink_size VARCHAR(20) NOT NULL,
    extras VARCHAR(50) NOT NULL,
    price NUMERIC NOT NULL """