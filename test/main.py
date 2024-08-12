import json
import os
from db import Connection
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
db = Connection('flask_mongo_crud')

MONGODBPW = os.getenv("MONGODBPW")
MONGODBUN = os.getenv("MONGODBUN")

CONNECTION_STRING = f"mongodb+srv://{MONGODBUN}:{MONGODBPW}@anmokuchi.lyunw.mongodb.net/?retryWrites=true&w=majority&appName=Anmokuchi"
client = MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')

@app.route('/')
def test():
    db.db.collection.insert_one({"name":"John"})
    return "success!"

if __name__ == '__main__':
    app.run(port=3000)

