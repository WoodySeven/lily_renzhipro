#!/usr/bin/env python
# @Author  : sally
import logging
import time
from selenium import webdriver
import unittest
import random
from selenium.webdriver.support.select import Select


class admin_create_order(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        driver = self.driver
        logging.info("打开浏览器成功")

    def tearDown(self):
        pass


    def test_create_product(self):
        logging.info("test_create_products start....")
        driver = self.driver
        url = self.base_url + "/ranzhi/www/sys/user-login.html"
        driver.get(url)
        driver.find_element_by_name('account').clear()
        driver.find_element_by_name('account').send_keys('admin')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('123456')
        time.sleep(2)
        if driver.find_element_by_id('keepLogin1').is_selected():
            driver.find_element_by_id('keepLogin1').click()
        driver.find_element_by_id('submit').click()
        time.sleep(3)
        # 定位到客户管理
        driver.find_element_by_xpath('//*[@id="s-menu-1"]/button').click()
        time.sleep(2)
        driver.maximize_window()
        # print(driver.current_url)
        # second_url='http://localhost/ranzhi/www/crm/dashboard/'
        # driver.get(second_url)
        driver.switch_to_frame('iframe-1')
        driver.find_element_by_link_text('订单').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()
        time.sleep(3)
        # 选择客户
        driver.find_element_by_xpath('//*[@id="customer_chosen"]/a').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="customer_chosen"]/div/ul/li[1]').click()
        # driver.find_element_by_xpath('//*[@id="customer_chosen"]/div/ul/li[3]').click()
        time.sleep(5)
        # 选择产品
        driver.find_element_by_xpath('//*[@id="createProduct"]').click()
        time.sleep(1)
        # 填写产品名称
        driver.find_element_by_xpath('//*[@id="productName"]').send_keys(random.choice('abcdefghjklqwertyuiomnbvcxz'))
        # 填写产品代号
        driver.find_element_by_xpath('//*[@id="code"]').send_keys("{0}{1}".format(random.choice('abcdefghjklqwertyuiomnbvcxz'), random.randint(1000, 9999)))
        # 选择产品线
        driver.find_element_by_xpath('//*[@id="line"]').click()
        time.sleep(2)
        # 输入计划金额
        driver.find_element_by_xpath('//*[@id="plan"]').send_keys('10000')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(2)




if __name__=="__main__":
    unittest.main