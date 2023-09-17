from utils.db import connect_to_mongodb
from quart import Quart, jsonify, Blueprint, request

auth= Blueprint('app_auth',__name__)
@auth.route('/rooms', methods=['GET'])
async def rooms() -> None:
    # login with username and return session token
    username = request.args.get("email")
    return jsonify(username=username, token="token")