#!/usr/bin/env python
# @Author  : sally
import logging
import time
import random
from nbformat import current
from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select


class admin_create_customer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        driver = self.driver
        logging.info("打开浏览器成功")

    def tearDown(self):
        pass

    def test_create_customer(self):
        logging.info("test_create_customer start....")
        driver = self.driver
        url = self.base_url + "/ranzhi/www/sys/user-login.html"
        driver.get(url)
        # 登陆
        driver.find_element_by_name('account').clear()
        driver.find_element_by_name('account').send_keys('admin')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('123456')
        time.sleep(2)
        if driver.find_element_by_id('keepLogin1').is_selected():
            driver.find_element_by_id('keepLogin1').click()
        driver.find_element_by_id('submit').click()
        time.sleep(3)
        #定位到客户管理
        driver.find_element_by_xpath('//*[@id="s-menu-1"]/button').click()
        time.sleep(2)
        driver.maximize_window()
        # print(driver.current_url)
        # second_url='http://localhost/ranzhi/www/crm/dashboard/'
        # driver.get(second_url)
        driver.switch_to_frame('iframe-1')
        driver.find_element_by_link_text('客户').click()
        time.sleep(3)
        #添加客户
        driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()
        time.sleep(2)
        driver.find_element_by_name('name').send_keys(random.randint(0,1000))
        driver.find_element_by_name('contact').send_keys('sally')
        driver.find_element_by_id('phone').send_keys(random.randint(10000000000,19999999999))
        time.sleep(2)
        driver.find_element_by_name('email').send_keys("{}@qq.com".format(random.randint(10000000,99999999)))
        driver.find_element_by_name('qq').send_keys(random.randint(10000000,99999999))
        Select(driver.find_element_by_name("type")).select_by_value("national")
        Select(driver.find_element_by_name('size')).select_by_value("1")
        time.sleep(2)
        Select(driver.find_element_by_name('level')).select_by_value("A")
        driver.find_element_by_name('intension').send_keys("happy to buy")
        time.sleep(3)
        driver.find_element_by_id('submit').click()








if __name__=="__main__":
    unittest.main