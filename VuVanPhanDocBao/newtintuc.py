# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import os

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://genk.vn/tin-ict.chn")
    # load wait page
    knswlist = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "knsw-list"))
    )

    li_elms = knswlist.find_elements_by_tag_name("h4")
    for li_elm in li_elms:
        try:
            class_ = li_elm.get_attribute("class")
            if "knswli-title" in class_:
                a_elm = li_elm.get_attribute('innerHTML')
                print a_elm.split("title=\"")[1].split("\"")[0]
                print "http://genk.vn/"+a_elm.split("href=\"")[1].split("\"")[0]
                print "\n"
        except NoSuchAttributeException as err:
            print 'Xin thu lai !!!'
            # kill all chromedriver
            os.system("pkill chromedriver")
            os.system("pkill chrome")

    # kill all chromedriver
    os.system("pkill chromedriver")
    os.system("pkill chrome")