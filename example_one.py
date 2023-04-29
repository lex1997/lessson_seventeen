import json

import requests
from consts import *

geturl = BASE_URL + TOKEN + '/getUpdates'
sendurl = BASE_URL + TOKEN + '/sendMessage'


class InlineKeyboardButton:
    def __init__(self):
        self.text = 'Button'


class InlineKeyboardMarkup:
    def __init__(self):
        self.keyboard = [InlineKeyboardButton().__getattribute__('text')]


def main():
    offset = 0
    timeout = 3
    while True:
        dt = dict(offset=offset, timeout=timeout)
        try:
            req = requests.post(geturl, data=dt, timeout=None).json()
        except ValueError:
            continue
        if not req['ok'] or not req['result']:
            continue
        for r in req['result']:
            message = r['message']
            id = message['chat']['id']
            if 'text' in message.keys():
                keyboard = json.dumps({'inline_keyboard': [[{'text': 'Yes', 'callback_data': 1}, {'text': 'google', 'url': 'www.google.com'}]]})
                dt = dict(chat_id=id, text='reply', reply_markup=keyboard)
                print(keyboard, dt)
                requests.post(sendurl, data=dt).json()
            offset = r['update_id'] + 1


if __name__ == '__main__':
    main()
