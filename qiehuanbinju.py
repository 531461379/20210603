from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/24 16:38

import requests
import time
import json
import os


class Spider():

    def __init__(self):
        self.url1 = "https://{}.talk-cloud.net/ClientAPI/getconfig"
        self.url2 = "https://global.talk-cloud.net/ClientAPI/getserverarea"
        self.data = {"serial":"981527802","userrole":0,"coursename":"thljhebct"}


    def getserver(self):
        res = requests.get(self.url2,timeout=0.5)
        res_json = json.loads(res.text)
        json_serverarealist = res_json.get("serverarealist")
        for i in json_serverarealist:
            servernames = i.get("serverareaname")
            print(servernames)
            # url_wanzheng = servernames+url_config
            # os.system("ping -n 1 %s"%url_wanzheng)


    # def getconfig(self):
    #     res = requests.get(self.url1.format(self.getserver()),self.data,timeout=1)
    #     new_json = json.loads(res.text)
    #     newcour_seaddrs = new_json.get("newcourseaddr")[0]
    #     change = newcour_seaddrs.get("change")
    #     print(change)






aaa = Spider()
# aaa.getconfig()
aaa.getserver()
