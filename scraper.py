import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from twilio.rest import Client
import time


def format_message(post):
    return "New post: " + post['title'] + "\n" + post['link']

if __name__ == '__main__':
    # Initial Mongo client
    db_client = MongoClient()

    # Configure API CLient
    account_sid = "AC848ff86eed3b049b877af8b98620f2f9"
    auth_token = "8394ad195a5c6bdca94bb79414db1429"
    client = Client(account_sid, auth_token)

    # get raw html of the web page through requests module
    hvq = requests.get("http://daotao.naem.edu.vn/")

    #Parse it to BeautifulSoup Tree
    soup = BeautifulSoup(hvq.text, "lxml")
    list_post = soup.find_all("div", class_="list-group-item")

    # Cleaning data
    extracted = []
    for x in list_post:
        if x.a is not None:
            extracted.append({
                "title": x.a.string,
                "link": "http://daotao.hvqlgd.edu.vn" + x.a.get('href')
            })
    # Save to database
    for post in extracted:
        if db_client.my_db.posts.find_one({"link": post["link"]}) is None:
            print("Found a new news at the following url: ", post['link'])
            message = format_message(post)
            client.messages.create(
                to="+84973706583",
                from_="+13238707831",
                body=message
            )
            db_client.my_db.posts.insert(post)

            # Sleep to avoid spam block
            time.sleep(10)

