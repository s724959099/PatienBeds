from flask import Flask, request, abort
from line_api import *
from manager import events_excute

app = Flask(__name__)


@app.route("/", methods=['POST', "GET"])
def index():
    return "Text"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    handler.handle(body, signature)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    events_excute(event)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
