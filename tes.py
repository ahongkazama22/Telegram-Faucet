import requests

cookies = {
    'captcha': 'recaptchav3',
    'twk_idm_key': 'YCz-AyTSHohRtXbvsKT0C',
    '_ga': 'GA1.1.1157046068.1705804420',
    '_gcl_au': '1.1.2031018674.1705804422',
    'bitmedia_fid': 'eyJmaWQiOiIxMWFlNTJiOTM5MTdlNTAzOGJmNDNkNmY1YzYzNGU1ZiIsImZpZG5vdWEiOiI3NmE5ZDNmZWU4NmIyZDA1MGE0ZWU0NTIzZTMxMjlmZSJ9',
    'TawkConnectionTime': '0',
    'twk_uuid_657ad8a407843602b801eed2': '%7B%22uuid%22%3A%221.bJriqljF2FeHlGuQ9QB39la47QQUDjdXcSXqMU2nZRecXffkJBdxX38mzxruE1FrlIYcmJnx9bQzmem9z2x6gUUWx6eTWEMtZK3qnrFnn0TTHV8nXmXK1TSX7VIUZ%22%2C%22version%22%3A3%2C%22domain%22%3A%22cryptofuture.co.in%22%2C%22ts%22%3A1705807796410%7D',
    'CoinTrafficPnd0': '1',
    'csrf_cookie_name': 'e9ef219d0f2d88f31d08d61e72f75be1',
    'ci_session': '908694d4fe0ac27509a984200e4bc4c94d0b3909',
    '_ga_E3ZTDBRNN5': 'GS1.1.1705804419.1.1.1705808401.0.0.0',
    'cf_clearance': 'gP2NMkwCoKMY3p00YMZ4uTUFnTnE71UGhkRUunOKt_A-1705808413-1-AT3OToTEN3WuGeNpZWRtHY5P4/eCq8qDIgXafDVvICVxBRtrOeT1Gd0uYkcws25VIwBu5wDJQqz11qB/sUPF/0U=',
    '_ga_VQ6N3SDNJY': 'GS1.1.1705804420.1.1.1705808422.0.0.0',
}

headers = {
    'authority': 'cryptofuture.co.in',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'captcha=recaptchav3; twk_idm_key=YCz-AyTSHohRtXbvsKT0C; _ga=GA1.1.1157046068.1705804420; _gcl_au=1.1.2031018674.1705804422; bitmedia_fid=eyJmaWQiOiIxMWFlNTJiOTM5MTdlNTAzOGJmNDNkNmY1YzYzNGU1ZiIsImZpZG5vdWEiOiI3NmE5ZDNmZWU4NmIyZDA1MGE0ZWU0NTIzZTMxMjlmZSJ9; TawkConnectionTime=0; twk_uuid_657ad8a407843602b801eed2=%7B%22uuid%22%3A%221.bJriqljF2FeHlGuQ9QB39la47QQUDjdXcSXqMU2nZRecXffkJBdxX38mzxruE1FrlIYcmJnx9bQzmem9z2x6gUUWx6eTWEMtZK3qnrFnn0TTHV8nXmXK1TSX7VIUZ%22%2C%22version%22%3A3%2C%22domain%22%3A%22cryptofuture.co.in%22%2C%22ts%22%3A1705807796410%7D; CoinTrafficPnd0=1; csrf_cookie_name=e9ef219d0f2d88f31d08d61e72f75be1; ci_session=908694d4fe0ac27509a984200e4bc4c94d0b3909; _ga_E3ZTDBRNN5=GS1.1.1705804419.1.1.1705808401.0.0.0; cf_clearance=gP2NMkwCoKMY3p00YMZ4uTUFnTnE71UGhkRUunOKt_A-1705808413-1-AT3OToTEN3WuGeNpZWRtHY5P4/eCq8qDIgXafDVvICVxBRtrOeT1Gd0uYkcws25VIwBu5wDJQqz11qB/sUPF/0U=; _ga_VQ6N3SDNJY=GS1.1.1705804420.1.1.1705808422.0.0.0',
    'origin': 'https://cryptofuture.co.in',
    'referer': 'https://cryptofuture.co.in/faucet/currency/btc',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}

data = {
    'csrf_token_name': 'e9ef219d0f2d88f31d08d61e72f75be1',
    'token': 'c7AKeYjgVxoMEvXFGJ2ayRq98sUzLH',
    'captcha': 'recaptchav3',
    'recaptchav3': '03AFcWeA7Orx-b7zPs197c8cUwDvYpIxoQQJS3RmJQcRwWcnyQ7BPu4cKl6vlW5MKvb78z6ywQGy-OYVptC8s_GVSvgjO8l7hNdoZ7E5FKu8M0bkPWTSrwxCx5zu5sEYBGNAAeB7WxxZbHOHwH5eZ5GNzlGEgWkBcf-usaWdpj-umz-50stXfugqg2y8rHVcYmCEVZJxqriCOfCuTVIcIunGb-rvjvqtAHWb5gBJiLIswCMaElkTOvlG9pEODI5lc89zC9v5nY6wnGF_oIV-qnK-KH6djdZs8f5PN6oS-tXZrpb6puRMfpaPtWhWU1WzwTOEZPO0cvxFSaBz3hOiYpIPGIYTTWi56sK41wSo9dRgdIbKDaVHU27uDIVwDg_gTx9yGExgZEohqBQns-gozetnftWGX_pDz-bKgRpfEo5lOZ8JNuJzs7vPyM__8gLXDJEOG4UPQWwyPhyEwzpUccbUs_pTLDutRxn6kKZckooploS_fncSeVMpcSEbM57uqMHnBQnHye3m-8Y_DCAe-IYkHP9zXQjwRdeK56H6r9WwJCySJGTO-mn4PUcboxqvmQ3GDE0M8jvvaY1TK7FvMkHh1blW6GJ9_W1T9y3xaO1V-_NTsiFcnqTBA',
    'wallet': 'sobatpeterpan55@gmail.com',
}

response = requests.post('https://cryptofuture.co.in/faucet/verify/btc', cookies=cookies, headers=headers, data=data)

print(response.text)