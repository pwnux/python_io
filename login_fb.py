from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.facebook.com/")

    def test_login(self):
        driver = self.driver
        #Nhap username fb
        facebookUsername = ""
        #Nhap password fb
        facebookPass = ""

        emailFieldID    = "email"
        passFieldID     = "pass"
        btnLoginID      = "loginbutton"
        logoXpath       = "(//a[contains(@href,'logo')])[1]"

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement  = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        btnLoginElement   = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(btnLoginID))

        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPass)
        btnLoginElement.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logoXpath))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()