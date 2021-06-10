import requests

#  get GCLB, route...

headers = {
    'Host': 'gateway.ebay-kleinanzeigen.de',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': '*/*',
    'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Access-Control-Request-Method': 'GET',
    'Access-Control-Request-Headers': 'authorization',
    'Referer': 'https://www.ebay-kleinanzeigen.de/',
    'Origin': 'https://www.ebay-kleinanzeigen.de',
    'Te': 'trailers',
    'Connection': 'close',
}

params = (
    ('include', '_meta'),
)

response = requests.options('https://gateway.ebay-kleinanzeigen.de/messagebox/api/users/76418625/conversations', headers=headers, params=params)
print(response.cookies.get_dict())
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('$https://gateway.ebay-kleinanzeigen.de/messagebox/api/users/76418625/conversations?include=_meta', headers=headers, verify=False)
