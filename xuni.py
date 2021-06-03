import requests


# url = "https://global.talk-cloud.net/WebAPI/setVirtualBg"
# data = {"key":"8iLAXnJlx8Ti9y77",
#         "serial":"1976837502",
#         "virtual_bg_id":425,
#         }
# res = requests.post(url=url,data=data)
# print(res.text)

# url1 = "https://demo.talk-cloud.net/WebAPI/virtualBgList"
# data1 = {"key":"4Qe3NWuVxwYxT7Tx",
#         # "serial":"1253693761",
#         # "virtual_bg_id":193,
#         }
# res1 = requests.post(url=url1,data=data1)
# print(res1.text)
#
url = "https://global.talk-cloud.net/WebAPI/virtualBgList"
data = {"key":"uQIfZ30vx5vkna70",
        "serial":"955012975",
        }
res = requests.post(url=url,data=data)
print(res.text)

#删除
# url = "https://global.talk-cloud.net/WebAPI/delVirtualBg"
# data = {"key":"8iLAXnJlx8Ti9y77",
#         "virtual_bg_id":419
#         }
# res = requests.post(url=url,data=data)
# print(res.text)