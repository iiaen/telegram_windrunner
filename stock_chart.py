from telethon.sync import TelegramClient 
from telethon import TelegramClient, sync, events 
from credentials import api_id, api_hash, bot_token, phone


# creating a telegram session and assigning it to a variable client 
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
   
# connecting and building the session 
client.connect() 
client.send_message('iiaen', 'Send message to @<bot> without signing in with OTP') 
client.send_file('iiaen', 'SWRD.png') 