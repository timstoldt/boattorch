import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

# client info (boattorch, torchcabin, etc)
conn.execute("""CREATE TABLE client (
                ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                usrName TEXT, 
                firstName TEXT,
                lastName TEXT,
                email TEXT,
                password TEXT,
                phone TEXT,
                squareID TEXT
                )""")

# credit card info
conn.execute("""CREATE TABLE ccInfo (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                nameOnCard TEXT, 
                cardNumber TEXT, 
                expireDate TEXT,  
                ccv TEXT, 
                zipCode TEXT
                )""")
                
# Figure Out necessary columns for this table
conn.execute("""CREATE TABLE squareInfo (
                ID INTEGER PRIMARY KEY AUTOINCREMENT
                )""")


conn.execute("""CREATE TABLE rentalObjects (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                clientID INTEGER,
                rateID INTEGER,
                name TEXT
                )""")

conn.close()
