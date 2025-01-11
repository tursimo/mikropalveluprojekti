import requests
import os
from flask import Flask
from flask import request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = '/usr/src/app/data/app.db'

def db_open():
    connection = sqlite3.connect(DATABASE)
    connection.execute('CREATE TABLE IF NOT EXISTS writings (title TEXT, writing TEXT)') 
    return connection

@app.route('/')
def getWritings():
    connection = db_open()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM writings')
    writings = cursor.fetchall()
    connection.close()
    print(writings)
    return f'Writings: {writings}'

@app.route('/send')
def setWriting():
    title = request.args.get('title')
    writing = request.args.get('writing')

    connection = db_open()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO writings (title, writing) VALUES (?, ?)',(title, writing))
    connection.commit()
    connection.close()
    return 'successfully inserted ' + title + ': ' + writing

if __name__ == "__main__":
    app.run(debug=True)