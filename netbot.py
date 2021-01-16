import os, httpx, json, time
from flask import abort, Flask, jsonify, request

from functions import get_devices, filter_devices


app = Flask(__name__)


def is_request_valid(request):
    is_token_valid = request.form["token"] == os.environ["SLACK_VERIFICATION_TOKEN"]
    is_team_id_valid = request.form["team_id"] == os.environ["SLACK_TEAM_ID"]

    return is_token_valid and is_team_id_valid


@app.route("/netbot", methods=["POST"])
def netbot():
    """ Parse & Validate command / parameters """

    # Ensure request is valid
    if not is_request_valid(request):
        print("Hit an Error")
        abort(400)

    # Save params to vars
    text = request.form.get("text", None)
    command = request.form.get("command", None)
    response_url = request.form.get("response_url", None)

    # return "Processing your request..."

    if text == "get devices":
        devices = filter_devices()
        my_response = {
            "response_type": "in_channel",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "```\n{}```".format("\n".join(devices[1:])),
                    },
                }
            ],
        }

    else:
        my_response = "Nothing to do"

    return my_response
