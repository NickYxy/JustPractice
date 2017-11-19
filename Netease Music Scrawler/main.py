import json
import requests
import time
from pymongo import *
from urllib import request
from urllib.parse import urlencode
from bs4 import BeautifulSoup


class NeteaseMusic:
    # 首先需要一个稳定可靠的header
    def __init__(self):
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Upgrade - Insecure - Requests': '1',
            'Referer': 'https://music.163.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.cookies = {'appver': '1.5.2'}
        db_name = 'mongo_music'
        client = MongoClient("mongodb://localhost:90713")
        self._db = client[db_name]

    # 然后我们需要对网页进行解析

    def search(self):
        url = 'https://music.163.com/#/playlist?id=14291453'
        params = {}
        response = requests.get(url=url, params=params, headers=self.headers)
