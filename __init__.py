#!/bin/python3
import urllib.request
import urllib.parse
import json

class ServerChan:
    API_URL = 'https://sc.ftqq.com/%s.send?%s'

    def __init__(self, serverchan_key):
        self.serverchan_key = serverchan_key

    def send(self, title, body=''):
        url = ServerChan.API_URL % (self.serverchan_key , urllib.parse.urlencode(dict(text=title, desp=body)))
        return json.loads(urllib.request.urlopen(url).read().decode('utf-8'))

class PushBear:
    API_URL = 'https://pushbear.ftqq.com/sub?%s'

    def __init__(self, send_key):
        self.send_key = send_key

    def send(self, title, body=''):
        url = PushBear.API_URL % (urllib.parse.urlencode(dict(sendkey=self.send_key, text=title, desp=body)))
        return json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
