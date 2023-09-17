import os
import random
import secrets

import pymongo
from dataclasses import asdict
from dotenv import load_dotenv
from api.models import Room, RoomMember, User
from quart import Quart, jsonify, request

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
    res = db.get_collection("users").find_one({"_id": email})
    if res:
        return jsonify(token=res["token"])
    else:
        token = secrets.token_urlsafe(32)
        names = ("John", "Andy", "Joe")
        new_user = User(
            _id=email,
            token=token,
            name=random.choice(names) + str(random.randint(1, 100)),
        )
        db.get_collection("users").insert_one(asdict(new_user))
        return jsonify(token=token)


@app.route("/rooms", methods=["POST", "GET"])
async def rooms() -> None:
    user_token = request.headers.get("token")
    # get user's email from token
    user = db.get_collection("users").find_one({"token": user_token})
    if not user:
        raise Exception("Invalid token")
    if request.method == "POST":
        # create a new room
        try:
            name, type, length = (
                request.args.get("name"),
                request.args.get("type"),
                request.args.get("length"),
            )
            new_roommember = RoomMember(_id=user["_id"], name=user["name"], progress=0)
            new_room = Room(
                _id=secrets.token_urlsafe(8),
                name=name,
                type=type,
                length=length,
                members=[new_roommember],
            )
            db.get_collection("rooms").insert_one(asdict(new_room))
            return "", 201
        except Exception as e:
            import traceback

            print(traceback.format_exc())
            return str(e), 400
    else:
        # Retrieve the rooms that match the query
        rooms = db.get_collection("rooms").find(
            {"members": {"$elemMatch": {"_id": user["_id"]}}}
        )
        return jsonify(list(rooms))

@app.route("/room/<room_id>", methods=["GET"])
async def get_room_info(room_id):
    # Retrieve room information based on the provided room_id
    room = db.get_collection("rooms").find_one({"_id": room_id})
    
    if room:
        # Convert the room document to a dictionary
        room_info = dict(room)
        return jsonify(room_info)
    else:
        user_token = request.headers.get("token")
        # get user's email from token
        user = db.get_collection("users").find_one({"token": user_token})
        if not user:
            return "Invalid token", 400
        # get all rooms with user's email in members
        # Query to find all rooms where the RoomMember is a member=
        return jsonify({"error": "Room not found"}), 404

@app.route("/room/<room_id>", methods=["PUT"])
async def update_room_progress(room_id, user_id):
    # Retrieve the room based on the provided room_id
    room = db.get_collection("rooms").find_one({"_id"})
    user_token = request.headers.get("token")
    # get user's email from token
    user = db.get_collection("users").find_one({"token": user_token})
    if room:
        # Find the user with the specified user_id within the room's members
        user_to_update = next((member for member in room["members"] if member["user_id"] == int(user_id)), None)

        if user_to_update:
            # Update the user's progress
            new_progress = request.json.get("progress")
            user_to_update["progress"] = new_progress

            # Update the room document in the collection
            db.get_collection("rooms").update_one({"_id": int(room_id)}, {"$set": {"members": room["members"]}})
            return jsonify({"message": "Progress updated successfully"})
        else:
            return jsonify({"error": "User not found in the room"}), 404
    else:
        return jsonify({"error": "Room not found"}), 404

@app.route("/rooms/<code>/join", methods=["POST"])
async def rooms_code_join(code: str) -> None:
    # get room with code
    # code = request.args.get("code")
    if not code:
        return "No code provided", 400
    user_token = request.headers.get("token")
    user = db.get_collection("users").find_one({"token": user_token})
    if not user:
        return "Invalid token", 400
    # find the room with the code
    room = db.get_collection("rooms").find_one({"_id": code})
    if not room:
        return "Room not found", 404
    # check if user is already in room
    if any(member["_id"] == user["_id"] for member in room["members"]):
        return "User already in room", 400
    # add user to room
    new_roommember = RoomMember(_id=user["_id"], name=user["name"], progress=0)
    db.get_collection("rooms").find_one_and_update({'_id': code}, {"$set": {"members": room["members"] + [asdict(new_roommember)]}})
    return "", 201


if __name__ == "__main__":
    run()
