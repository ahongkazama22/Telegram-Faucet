import asyncio
from telethon import TelegramClient

api_id = 20385404
api_hash = '7e47ea46b036b5fa01097357360bcbff'
client0 = TelegramClient('w1', api_id, api_hash)

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

akun = [client0]
for client in akun:
    async def main():
        await client.send_message('Adclickersbot', '🎁 Faucet')   
for client in akun:
    loop = asyncio.get_event_loop()
    with client:
        client.loop.run_until_complete(main())
