#!/usr/bin/env python
# @Author  : sally
import logging
import time
from selenium import webdriver
import unittest
import random
from selenium.webdriver.support.select import Select


class admin_cashier_account(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        driver = self.driver
        logging.info("打开浏览器成功")

    def tearDown(self):
        pass


    def test_cashier_account(self):
        logging.info("test_cashier_account start....")
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
        # 定位到现金记账
        driver.find_element_by_xpath('//*[@id="s-menu-3"]/button').click()
        time.sleep(2)
        driver.maximize_window()
        driver.switch_to_frame('iframe-3')
        driver.find_element_by_link_text('收入').click()
        time.sleep(3)
        #记收入
        driver.find_element_by_xpath('//*[@id="menuActions"]/a[2]').click()
        time.sleep(3)
        #选择账号
        # driver.find_element_by_xpath('//*[@id="depositor"]').click()
        Select(driver.find_element_by_xpath('//*[@id="depositor"]')).select_by_value('1')
        time.sleep(2)
        #选择科目
        Select(driver.find_element_by_xpath('//*[@id="category"]')).select_by_value('1')
        #选择客户
        driver.find_element_by_xpath('//*[@id="trader_chosen"]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="trader_chosen"]/div/ul/li[2]').click()
        time.sleep(1)
        #选择合同
        Select(driver.find_element_by_xpath('//*[@id="contract"]')).select_by_value('1')
        time.sleep(2)
        #输入金额
        driver.find_element_by_name('money').clear()
        driver.find_element_by_name('money').send_keys('500')
        #选择经手人
        driver.find_element_by_xpath('//*[@id="handlers_chosen"]/ul').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="handlers_chosen"]/div/ul/li[1]').click()
        #选择产品
        driver.find_element_by_xpath('//*[@id="product_chosen"]/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="product_chosen"]/div/ul/li[2]').click()
        time.sleep(2)
        #选择时间
        driver.find_element_by_xpath('//*[@id="date"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/tfoot/tr/th').click()
        #填写说明
        driver.find_element_by_id('desc').send_keys('收入记账')
        driver.find_element_by_id('submit').click()
        time.sleep(2)

        #记支出
        driver.find_element_by_link_text('支出').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="menuActions"]/a[2]').click()
        time.sleep(2)
        #选择账户
        Select(driver.find_element_by_xpath('//*[@id="depositor"]')).select_by_value('1')
        time.sleep(2)
        # 选择科目
        Select(driver.find_element_by_xpath('//*[@id="category"]')).select_by_value('3')
        time.sleep(2)
        driver.find_element_by_id('objectType1').click()
        #填写商户
        # driver.find_element_by_xpath('//*//*[@id="trader_chosen"]/a').click()
        # time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="trader_chosen"]/div/ul/li/text()').click()
        #填写金额
        driver.find_element_by_name('money').send_keys('100')
        #选择经手人
        driver.find_element_by_xpath('//*[@id="handlers_chosen"]/ul').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="handlers_chosen"]/div/ul/li[1]').click()
        #选择时间
        driver.find_element_by_name('date').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/tfoot/tr/th').click()
        #填写说明
        driver.find_element_by_id('desc').send_keys('测试支出')
        driver.find_element_by_id('submit').click()
        time.sleep(2)










if __name__=="__main__":
    unittest.main