#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: amoblin <amoblin@gmail.com>
# file name: ghost-publish.py
# create date: 2014-08-30 16:14:13
# This file is created from $MARBOO_HOME/media/starts/default.py
# 本文件由 $MARBOO_HOME/media/starts/default.py 复制而来

import sys
import json
import requests

USERNAME = "INPUT YOUR USER NAME"
PASSWORD = "INPUT YOUR PASSWORD"
HOST = "http://localhost:2368"

GHOST_API_PRE = "/ghost/api/v0.1"
GHOST_API_AUTH = "/authentication/token"
GHOST_API_POSTS = "/posts"

class Ghost:
    def __init__(self):
        self.s = requests.session()
        self.get_access_token()

    def get_full_url(self, path):
        return "%s%s%s" % (HOST, GHOST_API_PRE, path)

    def get_access_token(self):
        params = {
            "grant_type": "password",
            "username": USERNAME,
            "password": PASSWORD,
            "client_id": "ghost-admin"
        }

        r = self.s.post(self.get_full_url(GHOST_API_AUTH), data=params)
        response_dict = r.json()
        self.access_token =  response_dict["access_token"]
        self.token_type = response_dict["token_type"]

    def get_posts(self):
        headers = {"Authorization": "%s %s" % (self.token_type, self.access_token)}
        payload = {"limit": 10}
        content = self.s.get(self.get_full_url(GHOST_API_POSTS), headers=headers, params=payload).json()
        return content

    def post_one(self, title, content):
        headers = {"Authorization": "%s %s" % (self.token_type, self.access_token)}
#        payload = {"object":{"title": title, "markdon": content, "author": USERNAME}, "options": "TBD"}
        payload = {}

        content = self.s.post(self.get_full_url(GHOST_API_POSTS), headers=headers, params=payload).json()
        return content

if __name__ == "__main__":
    if len(sys.argv) > 2:
        USERNAME = sys.argv[1]
        PASSWORD = sys.argv[2]

    if len(USERNAME) == 0 or len(PASSWORD) == 0:
        print("Arguments Error")
        sys.exit(1)

    ghost = Ghost()
    for post in ghost.get_posts()["posts"]:
        print post["title"]
    print ghost.post_one("测试", "# 本文通过%s发送" % __file__)
    
