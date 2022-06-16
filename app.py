import os
import json
from flask import Flask, request
from Bot.src import WhatsApp


app = Flask(__name__)

messenger = WhatsApp(os.getenv("TOKEN"))
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Invalid verification token"


if __name__ == "__main__":
    app.run(port=5000, debug=True)