# -*- coding: utf-8 -*-
import requests
import json


def jsonify(f):
    def wrapped(*args, **kwargs):
        return f(*args, **kwargs).json()

    return wrapped


class BotHandler:
    """
    Telegram Bot Handler, which use telegram API
    """

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    @jsonify
    def get_updates(self, limit=1, offset=-1, timeout=30):
        method = 'getUpdates'
        params = {'limit': limit, 'offset': offset, 'timeout': timeout}
        resp = requests.get(self.api_url + method, params)
        return resp  # .json()

    @jsonify
    def send_message(self, chat_id, text):
        method = 'sendMessage'
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'Markdown'}
        resp = requests.get(self.api_url + method, params)
        return resp  # .json()

    @jsonify
    def render_info(self, chat_id, icon_id, caption):
        method = 'sendPhoto'
        params = {'chat_id': chat_id, 'photo': 'http://openweathermap.org/img/w/' + icon_id + '.png',
                  'caption': caption, 'parse_mode': 'Markdown'}
        resp = requests.get(self.api_url + method, params)
        return resp

    def get_location(self, chat_id):
        body = {
            "chat_id": chat_id,
            "text": "If you want to know what is the weather in your city, please tell me where you are",
            "reply_markup": {
                "one_time_keyboard": True,
                "keyboard": [
                    [{
                        "text": "Send Location",
                        "request_location": True
                    }],
                    [{
                        "text": "Cancel",
                        "remove_keyboard": True
                    }]
                ]
            }
        }

        requests.post(self.api_url + 'sendMessage', json.dumps(body),
                      headers={'Content-Type': 'application/json'})
