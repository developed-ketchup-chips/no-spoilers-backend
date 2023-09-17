import pymongo
from quart import Quart
from dotenv import load_dotenv
from utils.db import connect_to_mongodb
import random
from quart import Quart, jsonify, Blueprint, request
import os
import secrets

app = Quart(__name__)
load_dotenv()
dbconn = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = dbconn.get_database("no-spoilers")

def run() -> None:
    app.run()

@app.route('/authenticate', methods=['POST'])
async def authenticate() -> None:
    # login with username and return session token
    email = request.args.get("email")
    res = db.get_collection("users").find_one({"email": email})
    if res:
        return jsonify(token=res["token"])
    else:
        token = secrets.token_urlsafe(32)
        names = ('John','Andy','Joe')
        db.get_collection("users").insert_one({"email": email, "token": token, "name": random.choice(names) + str(random.randint(1, 100))})
        return jsonify(token=token)
    

@app.route('/rooms', methods=['GET'])
async def rooms() -> None:
    # login with username and return session token
    db.get_collection("rooms").insert_one({"email": "test@test.com"})

if __name__ == "__main__":
    run()
