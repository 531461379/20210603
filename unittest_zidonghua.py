#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/14 10:58

import unittest
from selenium import webdriver
import time,os
import faker
fakes = faker.Faker

class Testcase(unittest.TestCase):

    def setUp(self):
        chrome_driver = r'E:/python/chromedriver'
        os.environ["webdriver.Chrome.driver"] = chrome_driver
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches",
                                       ['enable-automation'])  # 设置chrome浏览器的参数，使其不弹框提示（chrome正在受自动测试软件的控制）
        prefs = {'profile.default_content_setting_values.media_stream_camera': 1,
                 'profile.default_content_setting_values.media_stream_mic': 1,
                 'profile.default_content_setting_values.notifications': 1,
                 'profile.default_content_setting_values.geolocation': 1}
        # 设置chrome浏览器的参数，使其不弹框提示（是否保存密码）
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        option.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=option)
        self.driver.maximize_window()


    def tearDown(self):

        self.driver.quit()


    def test_first(self):
        self.driver.get("https://global.talk-cloud.net/1364152026/10032/1/0")
        self.driver.find_element_by_class_name("nickname").send_keys(fakes)
        self.driver.find_element_by_id("roompwd").send_keys(1)
        self.driver.find_element_by_xpath('//*[@id="submit_btn"]').click()



if __name__ == '__main__':
    unittest.main()


