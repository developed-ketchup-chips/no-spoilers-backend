from quart import Quart, jsonify, Blueprint, request

auth= Blueprint('app_auth',__name__)
@auth.route('/authenticate', methods=['POST'])
async def authenticate() -> None:
    # login with username and return session token
    username = request.args.get("username")
    return jsonify(username=username, token="token")
