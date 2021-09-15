from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbpersonal

#메인 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

#API





if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug = True)