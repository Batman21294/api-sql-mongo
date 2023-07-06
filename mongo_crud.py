import json

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, request, jsonify

uri = "mongodb+srv://deepjyotib:Snape%401993@cluster0.3ykmmry.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = Flask(__name__)

@app.route("/create_cluster",methods=["GET","POST"])
def create_cluster():
    if request.method=="POST":
        db = client[request.json["cluster"]]
        return "created cluster"


@app.route("/insert", methods=["GET", "POST"])
def create_collection():
    if request.method == "POST":
        collection = client[request.json["cluster"]][request.json["collection"]]
        return "created collection"

@app.route("/insert_record", methods=["GET", "POST"])
def insert_record():
    if request.method == "POST":
        name = request.json["name"]
        number = request.json["number"]
        client[request.json["cluster"]][request.json["collection"]].insert_one({name:number})
        return jsonify("record inserted")

if __name__=="__main__":
    app.run()
