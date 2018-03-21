#!/bin/python3
import urllib.request
import urllib.parse
import json

class ServerChan:

    SERVERCHAN_URL = 'https://sc.ftqq.com/%s.send?%s'

    def __init__(self, serverchan_key):
        self.serverchan_key = serverchan_key

    def send(self, title, body):
        url = ServerChan.SERVERCHAN_URL % (self.serverchan_key , urllib.parse.urlencode(dict(text=title, desp=body)))
        return json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
