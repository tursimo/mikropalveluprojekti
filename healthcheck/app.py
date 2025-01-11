import requests
import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MOCK_HOST = os.environ['MOCK_HOST']
MOCK_PORT = os.environ['MOCK_PORT']

DATA_HOST = os.environ['DATA_HOST']
DATA_PORT = os.environ['DATA_PORT']

SCRAP_HOST = os.environ['SCRAP_HOST']
SCRAP_PORT = os.environ['SCRAP_PORT']

@app.route('/')
def do_check():
    x = requests.get("http://" + MOCK_HOST + ":" + MOCK_PORT)
    y = requests.get("https://" + DATA_HOST + ":" + DATA_PORT)
    z = requests.get("http://" + SCRAP_HOST + ":" + SCRAP_PORT)
    return 'mock=' + str(x.status_code) + ', data=' + str(y.status_code) + ', scrap=' + str(z.status_code)

if __name__ == "__main__":
    app.run(debug=True)