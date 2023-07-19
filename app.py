from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
import os

app = Flask(__name__)
connection_str = "mongodb+srv://tanmaysomani2003:zWSGzuouJgD7BvEi@clustermain.oocsnks.mongodb.net/?retryWrites=true&w=majority"
database = "Pyth1"
db_collection = "learningtheslowway"


client = MongoClient[connection_str]
db = client[database]
collection = db[db_collection]


@app.route("/users", methods=["GET"])
def get_users():
    user = list(collection.find())
    print(dumps(user))


if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port=5000,debug=True)

@app.route('/users',methods=['POST'])