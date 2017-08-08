# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium import *
import time


import os


if __name__ == "__main__":
    id = raw_input("Enter your email or phone number: ")
    pwd = raw_input("Enter your password: ")
    friend = raw_input("enter your friend or group you want to download your document: ")
    userURL = "https://messenger.com/t/" + friend


    driver = webdriver.Firefox()
    driver.get("https://messenger.com")

    email = driver.find_element_by_name("email")
    password = driver.find_element_by_name("pass")
    form = driver.find_element_by_id('loginform')
    email.send_keys(id)
    password.send_keys(pwd)
    form.submit()
    time.sleep(5)
    driver.get(userURL)
    temps = driver.find_elements_by_class_name("_2a42")
    lst = []
    for temp in temps:
        link = temp.find_elements_by_tag_name("a")
        for item in link:
            if item.get_attribute("href"):
                driver2 = webdriver.Firefox()
                driver2.get(item.get_attribute("href"))

    os.system("pkill geckodriver")
