#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/6/5 16:52
import os
import requests
import pandas as pd
import time


class PortLine(object):
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.lis_line = []  # 定义一个空列表
        self.lis_ping = []

    def line_url(self):
        response = requests.post(self.url)
        try:
            result = response.json()
            server_name_list = [new.get('serverareaname') for new in result.get('serverarealist')]#返回域名
            return server_name_list
        except Exception as e:
            print('解析服务器名称失败，响应：{}'.format(response.text))

    def line_url2(self):
        for server_name in self.line_url():
            url = "http://{}2.talk-cloud.net//ClientAPI/getconfig/".format(server_name)#
            time.sleep(1)
            response = requests.post(url, data=self.data)
            try:
                result = response.json()
                for new in result.get('newcourseaddr'):
                    change = new.get('change')
                    res_line = "线路ip：{}，域名：{}2.talk-cloud.net".format(change, server_name)
                    self.lis_line.append(res_line)  # 将需要的值存入到列表中
                    print(res_line)

                    res = os.popen("ping {} -n 1".format(change)).read()
                    res_ping = '{}'.format(res)
                    print(res_ping)
                    print("="*60)
                    self.lis_ping.append(res_ping)
            except Exception as e:
                print('解析服务器ip失败，响应：{}'.format(response.text))
                return ''


if __name__ == '__main__':
    url_one = 'http://global.talk-cloud.net//ClientAPI/getserverarea'
    data = {
        "serial": "981527802",
        "userrole":0,
    }
    port_line = PortLine(url_one, data)
    server_name_list = port_line.line_url()
    if server_name_list:
        port_line.line_url2()

    # df = pd.DataFrame({'res_line': port_line.lis_line, 'res_ping': port_line.lis_ping})
    # df.to_csv('line.csv', index=False,encoding='utf_8_sig',sep=',')