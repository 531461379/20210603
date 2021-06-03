#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : aes.py
# @Author: zhangsansui
# @Date  : 2020/10/20

from Crypto.Cipher import AES
import base64
from binascii import b2a_hex, a2b_hex

# 如果text不足16位的倍数就用空格补足为16位
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# 加密函数
def encrypt(text):
    key = 'l97lLyiwpjB15d6u'.encode('utf-8')
    mode = AES.MODE_CBC
    iv = b'l97lLyiwpjB15d6u'
    text = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(text)
    # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
    return b2a_hex(cipher_text)


if __name__ == '__main__':
    e = encrypt("1111")  # 加密
    print(e)



# def aes_encode(data, key):
#     while len(data) % 16 != 0:  # 补足字符串长度为16的倍数
#         data += (16 - len(data) % 16) * chr(16 - len(data) % 16)
#     data = str.encode(data)
#     aes = AES.new(str.encode(key), AES.MODE_ECB)  # 初始化加密器
#     return str(base64.encodebytes(aes.encrypt(data)), encoding='utf8').replace('\n', '')  # 加密
#
#
# if __name__ == '__main__':
#     key = 'l97lLyiwpjB15d6u'  # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
#     data = "1111"  # 待加密文本
#
#     mi = aes_encode(data, key)
#     print("加密值：", mi)