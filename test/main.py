import json
import config
import os
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

CONNECTION_STRING = f"mongodb+srv://{config.MONGODBUN}:{config.MONGODBPW}@anmokuchi.lyunw.mongodb.net/?retryWrites=true&w=majority&appName=Anmokuchi"
client = MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
collection = db.collection

@app.route('/', methods=['GET'])
def get_all_data():
    data = list(collection.find({}))
    for item in data:
        item['_id'] = str(item['_id'])
    return jsonify(data)

print("PASSWORD: ",config.MONGODBPW)

if __name__ == '__main__':
    app.run(port=3000)

