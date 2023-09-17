from quart import Quart
from dotenv import load_dotenv
from api.auth import auth

app = Quart(__name__)
app.register_blueprint(auth)

def run() -> None:
    app.run()

if __name__ == "__main__":
    load_dotenv()
    run()
