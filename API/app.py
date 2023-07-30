#!/usr/bin/env python
# encoding: utf-8
import json
import collections
import sqlite3 as sql
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/getClientName')
def index():
    con = sql.connect(addr)
    con.row_factory = sql.Row

    cur = con.cursor()
    userRows = cur.execute("select * from users").fetchall()

    # Convert query to objects of key-value pairs
    jsonArr = collections.OrderedDict()

app.run()