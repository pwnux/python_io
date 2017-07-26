# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import os


if __name__ == "__main__":

    driver = webdriver.Firefox()
    driver.get("http://sis.hust.edu.vn")

    try:
        # td_tb_dk_hoc = driver.find_element_by_id("MainContent_Thông báo đăng ký học tập_ICell")
        # tr_sis_theme = td_tb_dk_hoc.find_elements_by_class_name("dxncItem_SisTheme")
        #
        # for tr_sis_theme_elm in tr_sis_theme:
        #     date_create = tr_sis_theme_elm.find_element_by_class_name("dxncItemDate_SisTheme")
        #     print date_create.get_attribute("innerHTML")
        #     header_ = tr_sis_theme_elm.find_element_by_class_name("dxncItemHeader_SisTheme")
        #     print header_.find_element_by_tag_name("a").text

        page_pager = driver.find_element_by_id("MainContent_Thông báo đăng ký học tập_PGB")
        checking_first_page = True
        while True:

            td_tb_dk_hoc = driver.find_element_by_id("MainContent_Thông báo đăng ký học tập_ICell")
            tr_sis_theme = td_tb_dk_hoc.find_elements_by_class_name("dxncItem_SisTheme")

            for tr_sis_theme_elm in tr_sis_theme:
                date_create = tr_sis_theme_elm.find_element_by_class_name("dxncItemDate_SisTheme")
                print date_create.get_attribute("innerHTML")
                header_ = tr_sis_theme_elm.find_element_by_class_name("dxncItemHeader_SisTheme")
                print header_.find_element_by_tag_name("a").text
            checking_first_page = False

            # checking if false
            if not checking_first_page:
                # Blah blah blah
                print "Bat dau di tim pager"
                num_pages = page_pager.find_elements_by_tag_name("a")
                for num_pages_elm in num_pages:
                    num_pages_elm.click()
                    # break
                # break

    except NoSuchElementException as err:
        print "Khong ton tai, can xem lai"
        os.system("pkill geckodriver")

    os.system("pkill geckodriver")
