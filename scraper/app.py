import requests
import os
from flask import Flask
from flask import request
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PROTOCOL = os.environ['PROTOCOL']
MOCK_HOST = os.environ['MOCK_HOST']
MOCK_PORT = os.environ['MOCK_PORT']

@app.route('/')
def scrapePage():
    path = request.args.get('path', None)
    return scrape(PROTOCOL,MOCK_HOST,MOCK_PORT,path)

@app.route('/out')
def scrapeOutside():
    protocol = request.args.get('protocol')
    host = request.args.get('host')
    port = request.args.get('port', '')
    path = request.args.get('path', '')
    return scrape(protocol,host,port,path)

def scrape(proto,host,port,path=None):
    if path is None:
        page = requests.get(proto + "://" + host + ":" + port)
    else:
        page = requests.get(proto + "://" + host + ":" + port + "" + path)

    soup = BeautifulSoup(page.content, 'html.parser')
    list(soup.children)

    return soup.find_all('p')[0].get_text()

if __name__ == "__main__":
    app.run(debug=True)