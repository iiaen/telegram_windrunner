#!/usr/bin/python3
from telethon.sync import TelegramClient 
from telethon import TelegramClient, sync, events 
from credentials import api_id, api_hash, bot_token, username
import datetime
from PIL import Image

weekno = datetime.datetime.today().weekday()


def check_and_send(filename, caption):
    im = Image.open(filename)
    if im.size[1] > 5:
        client.send_file(username, filename, caption=caption) 


# 5 Sat, 6 Sun
if weekno > 0 and weekno < 5:
    # telegram session
    client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
    # client.parse_mode = 'html'
    client.connect() 

    # send tables
    check_and_send('openinsider.png', "Insider Purchases") 
    check_and_send('portfolio.png', "Yahoo Finance")
    check_and_send('candlestick.png', "MSFT Intraday") 
    # client.send_message(username, 'Send message to @<bot> without signing in with OTP') 


print('shish kebab')