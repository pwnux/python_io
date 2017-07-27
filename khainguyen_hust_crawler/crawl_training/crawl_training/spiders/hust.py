# -*- coding: utf8 -*-
__author__ = 'khainguyen'

import logging
import scrapy
from scrapy.http import TextResponse
from selenium import webdriver
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.common.by import By
from crawl_training.settings import TOR_PORT, TOR_IP
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

LOGGER.setLevel(logging.WARNING)


class Hust(scrapy.Spider):
    name = "hust"
    allowed_domains = ["http://sis.hust.edu.vn/"]
    start_urls = [
        "http://sis.hust.edu.vn/NewsModule/",
    ]
    parrent_title = ''

    def __init__(self):
        self.firefox_config()

    def firefox_tor_config(self):
        # connect with to via ip and port
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.proxy.type', 1)
        profile.set_preference('network.proxy.socks', TOR_IP)
        profile.set_preference('network.proxy.socks_port', TOR_PORT)
        # connect with tor via file tor local
        # self.driver = TorBrowserDriver('/home/tor-browser_en-US')
        self.driver = webdriver.Firefox(profile)

    def firefox_config(self):
        self.driver = webdriver.Firefox()

    def chrome_config(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=socks5://{}:{}'.format(TOR_IP,TOR_PORT))
        # turn off load image chrome
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def phantomjs_config(self):
        service_args = [
            '--proxy={}:{}'.format(TOR_IP,TOR_PORT),
            '--proxy-type=socks5',
        ]
        self.driver = webdriver.PhantomJS(service_args=service_args)

    def start_requests(self):
        self.driver.get(self.start_urls[0])
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located((By.ID, 'mainTextBody'))
        )
        response = TextResponse(url=self.start_urls[0], body=self.driver.page_source, encoding='utf-8')
        self.parse(response)

    def parse(self, response):
        for raw_url in response.xpath('//div[@id="dvNewsItem"]//a'):
            self.parrent_title = raw_url.xpath('text()').extract_first()
            url = response.urljoin(raw_url.xpath('@href').extract_first())
            self.driver.get(url)
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.ID, 'mainTextBody'))
            )
            response = TextResponse(url=url, body=self.driver.page_source, encoding='utf-8')
            self.parse_sub_element(response)

    def parse_sub_element(self, response):
        with open('data.txt','a') as file:
            file.write('-'*5 + 'Parrent title' + '-'*5 + '\n' + self.parrent_title + '\n')
            file.write('-'*5 + 'Sub title' + '-'*5 + '\n')
            for title in response.xpath('//div[@id="dvNewsItem"]//a/text()').extract():
                file.write(title + '\n')
