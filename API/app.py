import json
import collections
import sqlite3 as sql
from flask import Flask, jsonify

app = Flask(__name__)
addr = 'database/database.db'

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/addClient')
def add_client():
    try:
        con = sql.connect(addr)
        cur = con.cursor()
        cur.execute("INSERT INTO client (firstName) VALUES ('Tim')")
        con.commit()
        con.close()
        return 'Client added successfully!', 201
    except Exception as e:
        return str(e), 500

@app.route('/getClientName')
def get_client_name():
    try:
        con = sql.connect(addr)
        con.row_factory = sql.Row

        cur = con.cursor()
        userRows = cur.execute("SELECT * FROM client").fetchall()

        # Convert query to a list of dictionaries
        clients_Dict = {}
        for row in userRows:
            clients_Dict[row['ID']] = row['firstName']

        con.close()

        jsonOutput = json.dumps(clients_Dict, indent=4, sort_keys=True)
        return "<pre>" + jsonOutput + "</pre>", 201
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run()
