#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : xuxie.py
# @Author: zhangsansui
# @Date  : 2020/6/20

from ws4py.client.threadedclient import WebSocketClient
import json
import random
import threading
import requests


class CourtroomTest(object):

    def __init__(self, courtroom_num, people_num, addr='http://demo.talk-cloud.net:8889/'):
        self.courtroom_num = courtroom_num
        self.people_num = people_num
        self.config_url = 'http://demo.talk-cloud.net/ClientAPI/getconfig'

    @staticmethod
    def uuid():
        hex_li = list()
        hex_digits = '0123456789abcdef'
        for i in range(36):
            hex_li.append(random.choice(hex_digits))
        hex_li[8], hex_li[13], hex_li[18], hex_li[23] = '-', '-', '-', '-'
        return ''.join(hex_li)

    def courtroom_socket(self, room_id, hostname, port):
        properties = {
            'role': 2,
            'nickname': 'node_client',
            'watchStatus': 0,
            'publishstate': 0,
            'raisehand': False,
            'giftnumber': 0,
            'candraw': False,
            'disablevideo': False,
            'disableaudio': False,
            'pointerstate': False,
            'devicetype': 'WindowPC',
            'systemversion': 'chrome 62.0.3202.94',
            'version': '2.1.10',
            'volume': 100,
            'appType': 'webpageApp',
            'servername': "cn",
            'udpstate': 1,
            'hasvideo': False,
            'hasaudio': False
        }
        data =  {
            'userId': self.uuid(),
            'roomId': room_id,
            'maxVideo': 7,
            'videofps': 10,
            'videowidth': 176,
            'videoheight': 144,
            'properties': properties,
            'roomtype': 3,
            'version': 3,
        }
        # sock = websocket.WebSocket(socket.AF_INET, socket.SOCK_STREAM)
        ws = WebSocketClient("wss://demo.talk-cloud.net:8889/socket.io/?EIO=3&transport=websocket")
        # req="""{"joinRoom",{"userId":"f3531059-e818-63a1-fabe-2431fc831b6e","roomId":"1619042230","maxVideo":12,"videofps":10,"videowidth":320,"videoheight":240,"properties":{"role":0,"nickname":"laoshi","publishstate":0,"tk_screenstate":0,"tk_mediafilestate":0,"tk_enabledualstream":false,"hasvideo":false,"hasaudio":true,"raisehand":false,"giftnumber":0,"candraw":false,"disablevideo":false,"disableaudio":false,"pointerstate":false,"disablechat":false,"primaryColor":"#000000","devicetype":"WindowPC","systemversion":"chrome 81.0.4044.129","version":"3.3.6","appType":"webpageApp","volume":100,"tk_version":"2","tk_lowConsume":"1","codeVersion":2,"group":["defaultGroup"],"servername":"democn","tk_ip":"121.71.107.116","tk_area":"中国.北京.北京","tk_carrier":"鹏博士/电信"},"roomtype":3,"version":5,"vcodec":0,"develop":false,"questionCompatibility":false,"recordingSinceTeacherJoined":false}]}"""  #发送相应格式
        ws.send("joinRoom",data)
        ws.connect()
        ws.run_forever()

    def run(self):
        data = {
            'serial': self.courtroom_num,
            'selfip': '0.0.0.0',
        }
        session = requests.session()
        response = session.post(self.config_url, data=data)
        if response.status_code == 200:
            result = json.loads(response.text)
            hostname = result.get('newcourseaddr')[0].get('signaladdr')
            port = result.get('newcourseaddr')[0].get('signalport')
            # print(hostname, port)
            return hostname,port
        else:
            print('访问失败，响应状态吗：{}，响应内容：{}'.format(response.status_code, response.text))


if __name__ == '__main__':

    courtroom_num, people_num = input('请输入房间号和房间人数，用空格隔开：').split()  # 1663209371
    c_test = CourtroomTest(courtroom_num, people_num)
    hostname, port = c_test.run()
    # print(hostname)
    # print(port)
    for i in range(int(people_num)):
        c_test.courtroom_socket(courtroom_num, hostname, port)
