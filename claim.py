import time
import asyncio
import re
import webbrowser
from curl_cffi import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from telethon import TelegramClient, events

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
client21 = TelegramClient('w1', api_id, api_hash)


def RecaptchaV3():
    import requests
    ANCHOR_URL = 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcr1ncUAAAAAH3cghg6cOTPGARa8adOf-y9zv2x&co=aHR0cHM6Ly9vdW8ucHJlc3M6NDQz&hl=en&v=pCoGBhjs9s8EhFOHJFe8cqis&size=invisible&cb=ahgyd1gkfkhe'
    url_base = 'https://www.google.com/recaptcha/'
    post_data = "v={}&reason=q&c={}&k={}&co={}"
    client = requests.Session()
    client.headers.update({
        'content-type': 'application/x-www-form-urlencoded'
    })
    matches = re.findall('([api2|enterprise]+)\/anchor\?(.*)', ANCHOR_URL)[0]
    url_base += matches[0]+'/'
    params = matches[1]
    res = client.get(url_base+'anchor', params=params)
    token = re.findall(r'"recaptcha-token" value="(.*?)"', res.text)[0]
    params = dict(pair.split('=') for pair in params.split('&'))
    post_data = post_data.format(params["v"], token, params["k"], params["co"])
    res = client.post(url_base+'reload', params=f'k={params["k"]}', data=post_data)
    answer = re.findall(r'"rresp","(.*?)"', res.text)[0]    
    return answer

# -------------------------------------------
cookies = {
    '_ga': 'GA1.1.510402081.1705764082',
    '_ga_LVPHEL9V3B': 'deleted',
    'fpas': 's%3Aj%3A%2265818637ee2b890f674dc361%22.2XghF5MbeTiBvyC2Z27gQiCqKF4z1ro%2BcPSOnqqgfsI',
    'Se4Ry1Nr8': 's%3ABq0Ig5Ay4.HumAeWVEhV4Ai9XAVbfcvq7LVYqmwsjGGpMfj2BO9g8',
    'Ux0Br4Vj1': 's%3AIc5Pe7Fj5.evR8CR1eZE1x8I9WGlmdSACafNiA3JaQRBHdCsLZiSU',
    'Vz4Yv4Xh0': 's%3AUv5Pl3Ie2.ZCWXPEEpLhOzUk1FNaufm7hnxRY7SgFWdDvzGEMW%2Bq4',
    '_ga_LVPHEL9V3B': 'GS1.1.1706970652.11.1.1706970682.0.0.0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'id,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_ga=GA1.1.510402081.1705764082; _ga_LVPHEL9V3B=deleted; fpas=s%3Aj%3A%2265818637ee2b890f674dc361%22.2XghF5MbeTiBvyC2Z27gQiCqKF4z1ro%2BcPSOnqqgfsI; Se4Ry1Nr8=s%3ABq0Ig5Ay4.HumAeWVEhV4Ai9XAVbfcvq7LVYqmwsjGGpMfj2BO9g8; Ux0Br4Vj1=s%3AIc5Pe7Fj5.evR8CR1eZE1x8I9WGlmdSACafNiA3JaQRBHdCsLZiSU; Vz4Yv4Xh0=s%3AUv5Pl3Ie2.ZCWXPEEpLhOzUk1FNaufm7hnxRY7SgFWdDvzGEMW%2Bq4; _ga_LVPHEL9V3B=GS1.1.1706970652.11.1.1706970682.0.0.0',
    'Origin': 'https://adclickersbot.com',
    'Referer': 'https://adclickersbot.com/faucet-claim',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

client = requests.Session()
client.headers.update({
    'authority': 'ouo.io',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'referer': 'http://www.google.com/ig/adde?moduleurl=',
    'upgrade-insecure-requests': '1',
})

# -------------------------------------------
# OUO BYPASS


def ouo_bypass(url):
    tempurl = url.replace("ouo.press", "ouo.io")
    p = urlparse(tempurl)
    id = tempurl.split('/')[-1]
    res = client.get(tempurl, impersonate="chrome110")
    next_url = f"{p.scheme}://{p.hostname}/go/{id}"

    for _ in range(2):

        if res.headers.get('Location'): break

        bs4 = BeautifulSoup(res.content, 'lxml')
        inputs = bs4.form.findAll("input", {"name": re.compile(r"token$")})
        data = { input.get('name'): input.get('value') for input in inputs }
        data['x-token'] = RecaptchaV3()
        
        h = {
            'content-type': 'application/x-www-form-urlencoded'
        }
        
        res = client.post(next_url, data=data, headers=h, 
            allow_redirects=False, impersonate="chrome110")
        next_url = f"{p.scheme}://{p.hostname}/xreallcygo/{id}"

    return {
        res.headers.get('Location')
    }

akun = [client1, client2, client3, client4, client5, client6, client7, client8, client9, client10, client12, client13, client14, client15, client16, client17, client18, client19, client20, client21]

for clients in akun:
    clients.start() 
    for message in clients.iter_messages('adclickersbot', limit=1):
        if message.message == "🎁 Claim faucet every 15 minutes.":
            print(message.buttons[0][0].url)
            url = message.buttons[0][0].url
            h = {
                'content-type': 'application/x-www-form-urlencoded'
            }
            try :
                out = ouo_bypass(url)
            except :
                out = ouo_bypass(url)
            print(str(out)[2:(len(out)-3)])
            webbrowser.open(str(out)[2:(len(out)-3)])
            time.sleep(20)
