#_*_ coding:utf-8 _*_

import time
import logging
import datetime
import os

class Log():

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name = log_dir+"/"+log_file
        print(log_name)

        #文件输出日志
        self.file_handle = logging.FileHandler(log_name,"a",encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)


    def get_log(self):
        return self.logger


    def close_handle(self):

        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()




if __name__ == '__main__':
    log = Log()
    ll = log.get_log()
    ll.debug('test')