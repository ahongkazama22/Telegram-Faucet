import os
import time
import webbrowser
from telethon import TelegramClient, events
from PIL import Image
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
client12 = TelegramClient('82292', api_id, api_hash)
client13 = TelegramClient('kartu', api_id, api_hash)
client14 = TelegramClient('smartfren', api_id, api_hash)
client15 = TelegramClient('pardi', api_id, api_hash)
client16 = TelegramClient('axisser', api_id, api_hash)
client17 = TelegramClient('ayemtri', api_id, api_hash)
client18 = TelegramClient('dorangireng', api_id, api_hash)
client19 = TelegramClient('dorangputeh', api_id, api_hash)
client20 = TelegramClient('kabel', api_id, api_hash)

akun = [client1, client2, client3, client4, client5, client6, client7, client8, client9, client10, client12, client13, client14, client15, client16, client17, client18, client19, client20]
for client in akun:
     async def main():
          async for message in client.iter_messages('adclickersbot', limit=1):
               if message.media:
                    path = await message.download_media("kosong")
                    img = Image.open(path)
                    x =" ".join(pytesseract.image_to_string(img).split()).replace(" ","")
                    img.show()
                    print(x)
                    button1 = message.buttons[0][0]
                    button2 = message.buttons[0][1]
                    button3 = message.buttons[1][0]
                    button4 = message.buttons[1][1]
                    print(button1.text, button2.text, button3.text, button4.text)
               try:
                    if x[0:3].upper() <= button1.text.upper():
                         await button1.click()
                    elif x[0:3].upper() <= button2.text.upper():
                         await button2.click()
                    elif x[0:3].upper() <= button3.text.upper():
                         await button3.click()
                    elif x[0:3].upper() <= button4.text.upper():
                         await button4.click() 
                    elif eval(x) == button1.text:
                         await button1.click()
                    elif eval(x) == button2.text:
                         await button2.click()
                    elif eval(x) == button3.text:
                         await button3.click()
                    elif eval(x) == button4.text:
                         await button4.click()
                    else:
                         y = input()
                         if y=='1':
                              await button1.click()
                         elif y=='2':
                              await button2.click()
                         elif y=='3':
                              await button3.click()
                         elif y=='4':
                              await button4.click()
               except (RuntimeError, TypeError, NameError, SyntaxError):
                         pass
     with client:
          client.loop.run_until_complete(main())
     if os.path.exists("kosong.jpg"):
          os.remove("kosong.jpg")
     elif os.path.exists("kosong.gif"):
          os.remove("kosong.gif")