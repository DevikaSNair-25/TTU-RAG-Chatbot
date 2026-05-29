import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from chatbot import ask

app = Flask(__name__)

line_bot_api = LineBotApi("un7wUnW0tJDs00ydfjx52T/jIVOOM1XQOI3RbLWE48yEqNBOwNI3K8o0+sdMopfCN2B3EJqNrjjGRodFAKViGC9Ut6lCl13jW3ySr8tOC7NuYvLHjdobK9hplpeuT+P1h1dhcrcoTSQEkb/t7AJ9HwdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("4066c7c533696370b923efbf0d316759")

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    answer = ask(user_message)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=answer)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))