import os
import random
import secrets

import pymongo
from dotenv import load_dotenv
from models import Room, User
from quart import Blueprint, Quart, jsonify, request

app = Quart(__name__)
load_dotenv()
dbconn = pymongo.MongoClient(os.getenv("MONGO_URI"))
db = dbconn.get_database("no-spoilers")


def run() -> None:
    app.run()


@app.route("/authenticate", methods=["POST"])
async def authenticate() -> None:
    # login with username and return session token
    email = request.args.get("email")
    res = db.get_collection("users").find_one({"email": email})
    if res:
        return jsonify(token=res["token"])
    else:
        token = secrets.token_urlsafe(32)
        names = ("John", "Andy", "Joe")
        new_user = User(
            email=email,
            token=token,
            name=random.choice(names) + str(random.randint(1, 100)),
        )
        db.get_collection("users").insert_one(**new_user)
        return jsonify(token=token)


@app.route("/rooms", methods=["POST", "GET"])
async def rooms() -> None:
    if request.method == "POST":
        # create a new room
        try:
            name, type, length = (
                request.args.get("name"),
                request.args.get("type"),
                request.args.get("length"),
            )
            new_room = Room(name=name, type=type, length=length, members=[])
            db.get_collection("rooms").insert_one(**new_room)
            return "", 201
        except Exception as e:
            return str(e), 400



if __name__ == "__main__":
    run()
