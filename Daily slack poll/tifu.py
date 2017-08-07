#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slackclient import SlackClient

if __name__ == "__main__":
	slack_token = 'xoxp-11073699862-194273029174-204228475030-a85f0e8dbb5bb28a710d5f11ced8c716'
	sc = SlackClient(slack_token)
    sc.api_call(
        "chat.postMessage",
        channel='#swimming-fitness',
        username="Daily Poll",
        text="/ahem hôm nay ai đi bơi nhỉ?",
    )
