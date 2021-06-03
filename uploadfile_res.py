#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/2 14:35

import requests
import random
import unittest

#上传课件
while True:
    # aaa = random.randint(1000, 9999)
    url = "https://demo.talk-cloud.net/WebAPI/uploadfile"
    data = {"key":"4Qe3NWuVxwYxT7Tx",
            "serial":"1103241384",
            "conversion":1,
            "isopen":1,
            "dynamicppt":0,
            "isdefault":0,
            "companyid":0,
            "filecategory":0,
            # "sender":0,
            # "userid":0,
            # "h5docname":0,
            # "filenewname":0,
            # "notifyurl":0,
            "isconversion":0,
            "catalogid":0,
            "isvideoconversion":0,
            "isvideoalone":0,
            # "thirdroomid":"safsaf",
            # "thirdfileid":aaa,
            # "replacefileid":32746302,
            # "replacethirdfileid":"new_idss"
            }
    files = {'file':open(r"E:\wenjian\newfile.txt",encoding='utf8')}
    res = requests.post(url=url,data=data,files=files)
    print(res.text)

# #将其他服务器上的 H5 课件的 URL 上传
# url = "https://testing.talk-cloud.net/WebAPI/uploadFileUrl"
# data = {"key":"l97lLyiwpjB15d6u",
#         "serial":"1760842924",
#         "fileurl":"https://demodoc.talk-cloud.net/cospath/20201209_113254_szcswbsn/fileurl/测试.ppt",
#         "name":"ppts",
#         "thirdfileid":"newidss",
#         "replacefileid":"32746302",
#         "replacethirdfileid":"new_idss"
#         }
#
# res = requests.post(url=url,data=data)
# print(res.text)

# #关联课件
# url = "https://testing.talk-cloud.net/WebAPI/roombindfile"
# data = {"key":"l97lLyiwpjB15d6u",
#         "serial":"1760842924",
#         # "fileidarr[]":"32739291",
#         "fileid":"32739291",
#         "catalogidarr[]":"32739291",
#         "thirdfileidarr":"32739291"
#         }
#
# res = requests.post(url=url,data=data)
# print(res.text)

#取消关联
# url = "https://testing.talk-cloud.net/WebAPI/roomdeletefile"
# data = {"key":"l97lLyiwpjB15d6u",
#         "serial":1760842924,
#         "fileidarr[]":31981148,
#         "thirdfileidarr":"asfasfsa",
#         }
#
# res = requests.post(url=url,data=data)
# print(res.text)






