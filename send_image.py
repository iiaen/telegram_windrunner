#!/usr/bin/python3
from telethon.sync import TelegramClient 
from telethon import TelegramClient, sync, events 
from credentials import api_id, api_hash, bot_token, username
import datetime

weekno = datetime.datetime.today().weekday()

# 5 Sat, 6 Sun
if weekno > 0 and weekno < 6:
    # telegram session
    client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
    # client.parse_mode = 'html'
    client.connect() 

    # send tables
    client.send_file(username, 'openinsider.png', caption="Insider Purchases") 
    client.send_file(username, 'portfolio.png', caption="Yahoo Finance") 
    # client.send_message(username, 'Send message to @<bot> without signing in with OTP') 