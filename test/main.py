import json
import config
from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.decimal128 import Decimal128

app = Flask(__name__)

CONNECTION_STRING = f"mongodb+srv://{config.MONGODBUN}:{config.MONGODBPW}@anmokuchi.lyunw.mongodb.net/?retryWrites=true&w=majority&appName=Anmokuchi"
client = MongoClient(CONNECTION_STRING)
db = client.get_database('sample_airbnb')
collection = db.get_collection('listingsAndReviews')

def convert_decimal128_to_float(doc):
    for key, value in doc.items():
        if isinstance(value, Decimal128):
            doc[key] = float(value.to_decimal())
        elif isinstance(value, dict):
            doc[key] = convert_decimal128_to_float(value)
        elif isinstance(value, list):
            doc[key] = [convert_decimal128_to_float(item) if isinstance(item, dict) else item for item in value]
    return doc

@app.route('/', methods=['GET'])
def get_all_data():
    data = list(collection.find({}).limit(10))
    for item in data:
        item['_id'] = str(item['_id'])
        item = convert_decimal128_to_float(item)
    return jsonify(data)

print("PASSWORD: ",config.MONGODBPW)

if __name__ == '__main__':
    app.run(port=3000)

