import os
import json
from flask import Flask, request
from src.src import WhatsApp


app = Flask(__name__)

messenger = WhatsApp(os.getenv("TOKEN"))
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']



@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Invalid verification token"

    data = request.get_json()
    if not data:
        return "No data"
    else:
        fields = ['messages', 'text', 'interactive']
        for field in fields:
            if field in data:
                messenger.process_data(data)
                return "OK"
    # changed_field = messenger.changed_field(data)
    # if changed_field == "messages":
    #     new_message = messenger.get_mobile(data)
    #     if new_message:
    #         mobile = messenger.get_mobile(data)
    #         message_type = messenger.get_message_type(data)

    #         if message_type == "text":
    #             message = messenger.get_message(data)
    #             name = messenger.get_name(data)
    #             print(f"{name} with this {mobile} number sent  {message}")
    #             messenger.send_message(f"Hi {name}, nice to connect with you", mobile)

    #         elif message_type == "interactive":
    #             message_response = messenger.get_interactive_response(data)
    #             print(message_response)

    #         else:
    #             pass
    #     else:
    #         delivery = messenger.get_delivery(data)
    #         if delivery:
    #             print(f"Message : {delivery}")
    #         else:
    #             print("No new message")
    # return "ok"


if __name__ == "__main__":
    app.run(port=5000, debug=True)