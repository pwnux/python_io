# -*- coding: utf-8 -*-

import time

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import URL, USERNAME, PASSWORD


class AutoFacebook():
    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def sign_up(self, username, password):
        self.driver.get("http://facebook.com")

        self.driver.find_element_by_name('email').send_keys(username)
        self.driver.find_element_by_name('pass').send_keys(password)
        submit = self.driver.find_element_by_id('u_0_7')
        submit.submit()
        time.sleep(2)

    def load_message(self, url, message):
        self.driver.get(url)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.NAME, 'body'))
        )
        self.driver.find_element_by_name('body').send_keys(message)
        tmp = self.driver.find_element_by_name('send')
        tmp.click()


def load_data(index):
    with open('data.txt') as file:
        for line in file:
            if index in line:
                return line.replace(index, '')


if __name__ == "__main__":
    tmp = sys.argv[1]
    auto = AutoFacebook()
    auto.sign_up(USERNAME, PASSWORD)
    if tmp == 'test':
        auto.load_message(URL, 'Test success!')
    else:
        auto.load_message(URL, load_data(tmp))
