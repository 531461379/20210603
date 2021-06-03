#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/6/4 16:55


import requests
import os
import pandas as pd
import time


class PortLine(object):

    def __init__(self, url):
        self.url = url
        self.lis_line = []
        self.lis_ping = []
        # self.lis_line = []  # 定义一个空列表
        # self.lis_ping = []

    def line_url(self):
        res = requests.post(self.url).json()
        pri_text = [new.get('serverareaname') for new in res.get('serverarealist')]
        return pri_text

    def line_url2(self, url2, data):
        response = requests.post(url2, data=data).json()
        change = [new.get('change') for new in response.get('newcourseaddr')]
        return change


if __name__ == '__main__':

    url_one = 'http://global.talk-cloud.net//ClientAPI/getserverarea'
    port_line = PortLine(url_one)
    url1_list = port_line.line_url()

    for path in url1_list:
        url_three = "{}10.talk-cloud.net".format(path)
        url_two = "http://{}10.talk-cloud.net//ClientAPI/getconfig/".format(path)
        data = {"serial": "779440869", "selfip": "111.204.225.226"}
        domain_name = port_line.line_url2(url_two, data)
        print(domain_name,"线路ip")
        print(url_three)
        res = os.popen("ping {} -n 1".format(url_three)).read()
        print(res)
        print("="*60)
        # df = pd.DataFrame({'res_line': port_line.lis_line, 'res_ping': port_line.lis_ping})
        # df.to_csv('line.csv', index=False,encoding='utf_8_sig',sep=',')
