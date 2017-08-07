# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

homeLink = "http://tamlyhoctoipham.com/";
folderName = "E:\\tam ly hoc toi pham\\";

driver = webdriver.Firefox()

def getCategories():
    linkListCategories = []
    driver.get(homeLink)
    main_menu_id = driver.getElementById("main-menu").children().first()
    main_menu_list_item = main_menu_id.getElementsByTag("li")
    for main_menu_list_item_elem in main_menu_list_item:
        link = main_menu_list_item_elem.select("a").attr("href")
        if ("category" in link) and not (link in linkListCategories):
            linkListCategories.append(link)
    return  linkListCategories

def getAllArticlesFromCategory(categoryLink):
    linkListArticles =[]
    driver.get(categoryLink)
    currentLink = categoryLink

    while True:
        linkListArticles.addAll(getAllArticlesFromPage(driver))
        currentLink = linkNextPage(categoryLink, driver)
        if (currentLink != None):
            driver.get(currentLink)
        else:
            break
    else:
        break
    return linkListArticles


def getAllArticlesFromPage(driverCurentPage):
    linkListArticles = []
    articles_class = driver.getElementByClass("composs-blog-list lets-do-1")
    articles_header_item_class = articles_class.getElementsByClass("item-header")

    if (articles_header_item_class != None):
        for  article_header_item in( articles_header_item_class):
            article_link = article_header_item.select("a").attr("href")
            linkListArticles.append(article_link)

    return linkListArticles

def linkNextPage(curentCategory, curentDriver):
    pageIndex = curentDriver.getElementByClass("composs-panel-pager")
    hasNextPage = pageIndex.getElementByClass("next page-numbers")

    if (hasNextPage):
        currentPage =pageIndex.getElementsByClass("page-numbers current").text()
        nextPage = curentCategory+"?page="+str((int(currentPage)+1))
        return nextPage
    else:
        return None


def getContent(articleLink) :
    fileName = articleLink.replace(homeLink, "")


    driver.get(articleLink)
    content = driver.getElementByClass("composs-main-article-content")

    f = open(folderName + fileName + ".txt", "w")
    info = content.getElementByClass("composs-main-article-meta")
    title = content.getElementsByTag("h1").text()
    f.write("<p>"+title+"</p>\n")
    date = info.getElementByTag("span").text()
    if "access_time" in date:
        date = date.replace("access_time", "")
    f.write("<p>"+date+"</p>\n")
    f.close()

    f = open(folderName + fileName + ".html", "w")
    shortContentClass = content.getElementByClass("shortcode-content")
    f.write(shortContentClass)
    f.close()

def run():
    categories = getCategories()
	for category in categories:
		articles = getAllArticlesFromCategory(category)
		for article in articles:
			getContent(article)

run()