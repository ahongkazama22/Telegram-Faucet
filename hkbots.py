import os
import requests
import asyncio
import time
from colorama import init
from termcolor import colored
import webbrowser
from telethon.tl.functions.channels import JoinChannelRequest
from bs4 import BeautifulSoup
from telethon import TelegramClient, events
from PIL import Image
from telethon.sync import TelegramClient
from telethon import functions, types
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'


api_id = 20385404
api_hash = '7e47ea46b036b5fa01097357360bcbff'
client1 = TelegramClient('ahongkazama', api_id, api_hash)
client2 = TelegramClient('gajun', api_id, api_hash)
client3 = TelegramClient('kobot', api_id, api_hash)
client4 = TelegramClient('ibu', api_id, api_hash)
client5 = TelegramClient('andi', api_id, api_hash)
client6 = TelegramClient('endang', api_id, api_hash)
client7 = TelegramClient('gendon', api_id, api_hash)
client8 = TelegramClient('canadapandawa', api_id, api_hash)
client9 = TelegramClient('uangbulan', api_id, api_hash)
client10 = TelegramClient('lebak', api_id, api_hash)
client11 = TelegramClient('82292', api_id, api_hash)
client12 = TelegramClient('kartu', api_id, api_hash)
client13 = TelegramClient('smartfren', api_id, api_hash)
client14 = TelegramClient('pardi', api_id, api_hash)
client15 = TelegramClient('axisser', api_id, api_hash)
client16 = TelegramClient('ayemtri', api_id, api_hash)
client17 = TelegramClient('dorangireng', api_id, api_hash)
client18 = TelegramClient('dorangputeh', api_id, api_hash)
client19 = TelegramClient('kabel', api_id, api_hash)
client20 = TelegramClient('w1', api_id, api_hash)


akun = [client2]
init()
for client in akun:
  async def main():
    me = await client.get_me()
    print(colored((me.first_name,me.last_name),'red'))
    time.sleep(2)

    x=1
    while x==1:
      async for message in client.iter_messages('hkearn_usdt_bot', limit=1):
        #await message.buttons[0][1].click()
        time.sleep(3)
      print('visit site')
      await client.send_message('hkearn_usdt_bot', '/cancel')
      time.sleep(2)
      await client.send_message('hkearn_usdt_bot', '/earn')
      time.sleep(4)
      async for message in client.iter_messages('hkearn_usdt_bot', limit=1):
        print(message.text)
        await message.buttons[1][0].click()
      async for visit in client.iter_messages('hkearn_usdt_bot', limit=1):
        print(visit.text)
        try:
          if visit.text[0]=='🤚' :
            webbrowser.open(message.buttons[0][0].url)
            time.sleep(20)
            input('verify ???')
            async for verify in client.iter_messages('hkearn_usdt_bot', limit=1):
              if verify.text[0]=='🛡️' :
                await verify.buttons[0][1].click()
          if visit.buttons[0][0].url[0:28]=='https://www.hkbots.xyz/visit':
            await visit.buttons[0][0].click()
            time.sleep(10)
        except:
          pass
        if visit.text[0]=='😟':
          x=10


    y=1
    while y==1:
      print('Join Chats')
      await client.send_message('hkearn_usdt_bot', '/cancel')
      time.sleep(2)
      await client.send_message('hkearn_usdt_bot', '/earn')
      time.sleep(2)
      async for message in client.iter_messages('hkearn_usdt_bot', limit=1):
        await message.buttons[1][1].click()
      async for join in client.iter_messages('hkearn_usdt_bot', limit=1):
        print(join.text)
        try:
          if join.text[0]=='🤚' :
            webbrowser.open(message.buttons[0][0].url)
            time.sleep(20)
          if join.text[0]=='🛡️' :
            await join.buttons[0][1].click()
          if join.buttons[0][0].url[0:22]=='https://www.hkbots.xyz':
            await join.buttons[0][0].click()
            time.sleep(10)
          if join.buttons[0][0].url[0:12]=='https://t.me':
            result = await client(functions.channels.JoinChannelRequest(join.buttons[0][0].url[13:len(join.buttons[0][0].url)]))
            time.sleep(1)
            await join.buttons[0][1].click()
        except:
          pass
        if join.text[0]=='😟':
          y=10


    z=1
    while z==1:
      print('view posts')
      await client.send_message('hkearn_usdt_bot', '/cancel')
      time.sleep(2)
      await client.send_message('hkearn_usdt_bot', '/earn')
      time.sleep(2)
      async for message in client.iter_messages('hkearn_usdt_bot', limit=1):
        await message.buttons[2][0].click()
      async for visit in client.iter_messages('hkearn_usdt_bot', limit=1):
        print(visit.text)
        try:
          if visit.text[0]=='🤚' :
            webbrowser.open(message.buttons[0][0].url)
            time.sleep(20)
          if visit.text[0]=='🛡️' :
            await visit.buttons[0][1].click()
          if visit.text[0]=='👆' :
            await visit.buttons[0][0].click()
          if visit.buttons[0][0].url[0:22]=='https://www.hkbots.xyz':
            await visit.buttons[0][0].click()
        except:
          pass
        if visit.text[0]=='😟':
          z=10

    i=1
    while i==1:
      print('bot task')
      await client.send_message('hkearn_usdt_bot', '/cancel')
      time.sleep(2)
      await client.send_message('hkearn_usdt_bot', '/earn')
      time.sleep(2)
      async for message in client.iter_messages('hkearn_usdt_bot', limit=1):
        try:
          await message.buttons[1][2].click()
        except:
          pass
      async for bot in client.iter_messages('hkearn_usdt_bot', limit=2):
        print(bot.text)
        try:
          if bot.text[0]=='🤚' :
            webbrowser.open(message.buttons[0][0].url)
            time.sleep(20)
          if bot.text[0]=='🛡️' :
            await bot.buttons[0][1].click()
          if bot.buttons[0][0].url[0:22]=='https://www.hkbots.xyz':
            await bot.buttons[0][0].click()
            time.sleep(10)
          if bot.buttons[0][0].url[0:12]=='https://t.me':
            bot_link , refereal = bot.buttons[0][0].url.split('?')
            if bot_link=='':
              bot_link=bot.buttons[0][0].url
            await client.send_message(bot_link, '/start')
            time.sleep(3)
            async for terusan in client.iter_messages(bot_link, limit=1):
              await client.forward_messages('hkearn_usdt_bot', terusan,)
        except:
          pass
        try:
          await client.send_message(bot.buttons[0][0].url, '/start')
          time.sleep(3)
          print(bot.buttons[0][0].url[13:len(bot.buttons[0][0].url)])
          async for teruskan in client.iter_messages(bot.buttons[0][0].url, limit=1):
            await client.forward_messages('hkearn_usdt_bot', teruskan,)
        except:
          pass
        if bot.text[0]=='😟':
          i=10


for client in akun:
  loop = asyncio.get_event_loop()
  with client:
    client.loop.run_until_complete(main())