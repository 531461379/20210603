
import time
import requests
import hashlib
import random
from Crypto.Cipher import AES
from binascii import b2a_hex

AES_LENGTH = 16


url = "https://demo.talk-cloud.net/WebAPI/entry"
key = "ClxcwfkF1qUICqnR"   #authkey值
serial = "1000173314"    #房间号
usertype = "0"    #用户类型
domain = "yihuazhibo"   #企业域名
passwd = "pppppp"



randoms = random.randint(1000, 9999)
times = int(time.time())
auth = key+str(times)+serial+usertype
#userpassword参数,aes加密
aes_key = key
mode = AES.MODE_ECB
# 加密密钥需要长达16位字符，所以进行空格拼接
def pad_key(key):
    while len(key) % AES_LENGTH != 0:
        key += ' '
    return key
cryptor = AES.new(pad_key(aes_key).encode(), mode)

def pad(text):
    while len(text) % AES_LENGTH != 0:
        text += ' '
    return text


def encrypt(text):
    ciphertext = cryptor.encrypt(pad(text).encode())
    return b2a_hex(ciphertext)

def md5():
    md5_auth = hashlib.md5(auth.encode(encoding='UTF-8')).hexdigest()
    return md5_auth

def res_get():
    data = {"domain":domain, "serial":serial,
                 "username": "entry_serial", "usertype":usertype,
                 "pid":randoms,"ts":times, "auth":md5(),"userpassword":encrypt(passwd).decode(),"stuJumpUrl":"https://www.baidu.com/"}
    res = requests.get(url,data)
    print(res.url)

res_get()