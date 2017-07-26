# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import os
import time

def findSche(driver):
	try:
		td_tb_dk_hoc = driver.find_element_by_id("MainContent_Thông báo đăng ký học tập_CCell")
		tr_sis_theme = td_tb_dk_hoc.find_elements_by_class_name("dxncItem_SisTheme")
		for tr_sis_theme_elm in tr_sis_theme:
			day_create = tr_sis_theme_elm.find_element_by_class_name("dxncItemDate_SisTheme").get_attribute("innerHTML")
			header = tr_sis_theme_elm.find_element_by_class_name("dxncItemHeader_SisTheme")
			find_tag = header.find_element_by_tag_name('a').get_attribute("innerHTML")
			print  day_create,find_tag


	except NoSuchElementException as err:
		print "khong ton tai"
		os.system("pkill geckodriver")

def findPage(driver,val):
	try:
		td_pg_dk_hoc = driver.find_element_by_id("MainContent_Thông báo đăng ký học tập_PGB")
		pg_dk = td_pg_dk_hoc.find_elements_by_tag_name("a")
		pg_dk_cur_val = val
		if pg_dk is not None:
			for pg_dk_ele in pg_dk:
				if int(pg_dk_ele.get_attribute("innerHTML"))>pg_dk_cur_val:
					pg_dk_ele.click()
					findSche(driver)
					print "page",val+1
					print "--------------------------------------------"

					break
			else:
				print "END"
				return None
			findPage(driver, val + 1)


	except NoSuchElementException as err:
		print "khong thay"
		os.system("pkill geckodriver")

if __name__ == "__main__":

	driver = webdriver.Firefox()
	driver.get("http://sis.hust.edu.vn/")
	findSche(driver)
	print "page",1
	print "--------------------------------------------"
	findPage(driver,1)

	os.system("pkill geckodriver")

