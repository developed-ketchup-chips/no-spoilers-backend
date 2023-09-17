from quart import Blueprint, Quart, jsonify, request
from utils.db import connect_to_mongodb

auth = Blueprint("app_auth", __name__)


@auth.route("/rooms", methods=["GET"])
async def rooms() -> None:
    # login with username and return session token
    username = request.args.get("email")
    return jsonify(username=username, token="token")
