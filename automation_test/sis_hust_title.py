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

    main_text_body = driver.find_element_by_id("mainTextBody")
    tds_elm = main_text_body.find_elements_by_tag_name("td")
    for td_elm in tds_elm:
        td_style = td_elm.get_attribute("style")
        if "top;" in td_style and "70%" in td_style:
            elm_spans = td_elm.find_elements_by_tag_name("span")

            for elm_span in elm_spans:
                elm_span_style = elm_span.get_attribute("style")
                if "DarkRed" in elm_span_style:
                    print elm_span.get_attribute("innerHTML")
        else:
            break

    os.system("pkill geckodriver")
    os.system("pkill firefox")
