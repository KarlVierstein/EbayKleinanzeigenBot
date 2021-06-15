# with requests.Session() as s:
#    print(s.cookies.get_dict())
#    response = s.get('https://ebay-kleinanzeigen.de')
#    print(s.cookies.get_dict())


import requests

cookies = {
    '_ga': 'GA1.2.291931199.1622214046',
    'clientId': '291931199.1622214046',
    'ekConsentBucketTcf2': 'full2-exp',
    'iom_consent': '0103ff03ff&1622214078090',
    'ekConsentTcf2': '{%22customVersion%22:2%2C%22encodedConsentString%22:%22CPG6jl3PG6jl3E1ABADEBQCgAP_AAAAAAAYgHhNf_X_fb3_j-_59__t0eY1f9_7_v-0zjhfds-8N2f_X_L8X_2M7vF36pr4KuR4ku3bBIQdtHOncTUmx6olVrTPsbk2Mr7NKJ7Pkmnsbe2dYGH9_n93T_ZKZ7__v___7________7_______3_v_____-_____9___8AAABJSADAAEDwiUAGAAIHhEIAMAAQPCHQAYAAgeEMgAwABA8IVABgACB4QiADAAEDwg0AGAAIHhBIAMAAQPCA.YAAAAAAAASA%22%2C%22googleConsentGiven%22:true%2C%22consentInterpretation%22:{%22googleAdvertisingFeaturesAllowed%22:true}}',
    'overlayV21': 'seen',
    '__gads': 'ID=e8a0da3eb3714af0:T=1622214079:S=ALNI_MYjmTkl69U4L1qA3yqsPDpkQtognw',
    '_gid': 'GA1.2.2065273841.1622705475',
    'POPUPCHECK': '1622791875484',
    'up': '%7B%22ln%22%3A%22473390967%22%2C%22lln%22%3A%22f8a25dd7-a579-41be-b9bb-43b9251ccd0b%22%2C%22llstv%22%3A%2297-js-errorlog%3DA%7CBLN-18532_highlight%3DB%7CBLN-18275-lazy-load-image%3DA%7CDesktop_Test%3DA%7Creact-msgbox-payment-buy%3DB%7Creact-msgbox-payship%3DB%7CBLN-18685_auth_svr%3DA%7Cspeedcurve-labs-lux-1%3DA%7Cgdpr-experimental%3DB%7Cspeedcurve-labs-lux-2%3DA%7CBLN-18221_srp_rebrush_ads%3DB%7CBLN-18849-manage-ads-k8s%3DB%7C76-preact-header-footer%3DA%7CBLN-18727-TopAd-enabler%3DA%7C74-react-messagebox%3DA%7CEBAYKAD-2252_group-assign%3DB%22%2C%22ls%22%3A%22k%3Diphone%22%2C%22va%22%3A%221780565842%2C2378867%2C-17636599%2C17625574%2C2403904%22%2C%22vapwrncats%22%3A1%2C%22vapwrnscrty%22%3A1%7D',
    'uh': '%7B%22sh%22%3A%22k%3Diphone%3A%3Ak%3Djob%26c%3D102%26pt%3DPRIVATE%3A%3Ak%3Djob%26pt%3DCOMMERCIAL%3A%3Ak%3D4tb%2520hdd%3A%3Ak%3Diphone%26c%3D210%3A%3Ak%3Diphone%26c%3D161%22%7D',
    'ioam2018': '000ed90b73261135360b1059d:1648220446343:1622214046344:.ebay-kleinanzeigen.de:147:ebaykanz:ebayK-2:noevent:1622706111058:m8mpom',
}

headers = {
    'Host': 'www.ebay-kleinanzeigen.de',
    'Sec-Ch-Ua': '\\" Not A;Brand\\";v=\\"99\\", \\"Chromium\\";v=\\"90\\"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'close',
}

cookies_login = {
    'CSRF-TOKEN': '01d47efe-bf85-42e6-82d0-2f4a516a907e',
    'up': '%7B%22ln%22%3A%22606300982%22%2C%22lln%22%3A%229300df05-6423-4cce-b3e8-22e4cbd650d7%22%2C%22llstv%22%3A%2297-js-errorlog%3DA%7CBLN-18532_highlight%3DB%7CBLN-18275-lazy-load-image%3DA%7CDesktop_Test%3DB%7Creact-msgbox-payment-buy%3DB%7Creact-msgbox-payship%3DB%7CBLN-18685_auth_svr%3DA%7Cspeedcurve-labs-lux-1%3DB%7Cgdpr-experimental%3DC%7Cspeedcurve-labs-lux-2%3DB%7CBLN-18221_srp_rebrush_ads%3DB%7CBLN-18849-manage-ads-k8s%3DB%7C76-preact-header-footer%3DA%7CBLN-18727-TopAd-enabler%3DA%7C74-react-messagebox%3DA%7CEBAYKAD-2252_group-assign%3DA%22%2C%22ls%22%3A%22l%3D0%22%2C%22saSe%22%3A%22%22%7D',
    'GCLB': 'CJ7Fzr_LyJCu0AE',
    'rbzid': 'vVI7j/fPyXH4rXJ2iD4EynDdHUuh6iAORe2fSOGjs06CulmLwpAIFDoWR2MOQznzx6Pv/VjNeNPp7mRjzPSft3maXFuxY2xk0jlePInfM+jl8rlmBDh250MQoFQFQZbBcx8s2GftAPuSfbUcjJJXffDGtUGxHYka/G04NfqQwmLFxDRqliyybW8LKFMrCuTKxR6IoOlIHrQtoSDmGSmhkg==',
    'rbzsessionid': '0ab0a83d4b5bb7b8c365f94794cc1aff',
    'ioam2018': '0014660c08673577a60b8f62a:1653579178191:1622734378191:.ebay-kleinanzeigen.de:9:ebaykanz:ebayK-6:noevent:1622741114542:5rqtb0',
    'iom_consent': '0103ff03ff&1622734382291',
    '_ga': 'GA1.2.1575819242.1622734379',
    '_gid': 'GA1.2.1579947978.1622734379',
    'clientId': '1575819242.1622734379',
    'ekConsentTcf2': '{%22customVersion%22:2%2C%22encodedConsentString%22:%22CPHOZ3KPHOZ3KE1ABADEBQCgAP_AAAAAAAYgHhNf_X_fb3_j-_59__t0eY1f9_7_v-0zjhfds-8N2f_X_L8X_2M7vF36pr4KuR4ku3bBIQdtHOncTUmx6olVrTPsbk2Mr7NKJ7Pkmnsbe2dYGH9_n93T_ZKZ7__v___7________7_______3_v_____-_____9___8AAABISADAAEDwg0AGAAIHhCIAMAAQPCFQAYAAgeEMgAwABA8IdABgACB4RCADAAEDwiUAGAAIHhFIAMAAQPCA.YAAAAAAAASA%22%2C%22googleConsentGiven%22:true%2C%22consentInterpretation%22:{%22googleAdvertisingFeaturesAllowed%22:true}}',
    'ekConsentBucketTcf2': 'full2-exp',
    '__gads': 'ID=dd0634b32eb1c791-224f000156c8008c:T=1622741116:S=ALNI_MaHcLTHFB9U6gx4xkAu8SwGwBq-jQ',
    'overlayV21': 'seen',
    'wl': '%7B%22l%22%3A%22%22%7D',
    'sc': '%7B%7D',
    'POPUPCHECK': '1622820883139',
    'cto_bundle': 'zkMxmV9uUzRqZmlwTmVWT1k5ZEc3ZjB0ZHlOdGZxcDh2NU16Z2l3cVRqc0VsJTJGUUhWN29FajVMWjdZb3ZYY3dOMGluZkw5WUdIdkV6SCUyRlBvUU9yWU5WUXZYbjVuSXZDcCUyRnZNZ0VydER6cWJsY3BSQWdqZVFjUkFwbzQ0MGJJSVRVYkl6R0Q3dmR4THBmR0VKVjkyJTJGTHFkUG1zYkFJYXFDNjZxak1XNEFSWGs5SEUyJTJGZ1dBQ2xZejhWeXFFN1JidUNRSkRLQ25iazExVGxiVlFFemNJVmtrVzZZdyUzRCUzRA',
    '_gat': '1',
    'JSESSIONID': 'EA9B063144FBBF1CDDBF5EF4C4B04120-mc6.koeb47-22_i01_1001',
}

headers_login = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.ebay-kleinanzeigen.de',
    'Connection': 'keep-alive',
    'Referer': 'https://www.ebay-kleinanzeigen.de/m-einloggen.html?targetUrl=/',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers',
}


def login_headers(csrf_token):
    return {
        'CSRF-TOKEN': csrf_token,
        'up': '%7B%22ln%22%3A%22606300982%22%2C%22lln%22%3A%229300df05-6423-4cce-b3e8-22e4cbd650d7%22%2C%22llstv%22%3A%2297-js-errorlog%3DA%7CBLN-18532_highlight%3DB%7CBLN-18275-lazy-load-image%3DA%7CDesktop_Test%3DB%7Creact-msgbox-payment-buy%3DB%7Creact-msgbox-payship%3DB%7CBLN-18685_auth_svr%3DA%7Cspeedcurve-labs-lux-1%3DB%7Cgdpr-experimental%3DC%7Cspeedcurve-labs-lux-2%3DB%7CBLN-18221_srp_rebrush_ads%3DB%7CBLN-18849-manage-ads-k8s%3DB%7C76-preact-header-footer%3DA%7CBLN-18727-TopAd-enabler%3DA%7C74-react-messagebox%3DA%7CEBAYKAD-2252_group-assign%3DA%22%2C%22ls%22%3A%22l%3D0%22%2C%22saSe%22%3A%22%22%7D',
        'GCLB': 'CJ7Fzr_LyJCu0AE',
        'rbzid': 'vVI7j/fPyXH4rXJ2iD4EynDdHUuh6iAORe2fSOGjs06CulmLwpAIFDoWR2MOQznzx6Pv/VjNeNPp7mRjzPSft3maXFuxY2xk0jlePInfM+jl8rlmBDh250MQoFQFQZbBcx8s2GftAPuSfbUcjJJXffDGtUGxHYka/G04NfqQwmLFxDRqliyybW8LKFMrCuTKxR6IoOlIHrQtoSDmGSmhkg==',
        'rbzsessionid': '0ab0a83d4b5bb7b8c365f94794cc1aff',
        'ioam2018': '0014660c08673577a60b8f62a:1653579178191:1622734378191:.ebay-kleinanzeigen.de:9:ebaykanz:ebayK-6:noevent:1622741114542:5rqtb0',
        'iom_consent': '0103ff03ff&1622734382291',
        '_ga': 'GA1.2.1575819242.1622734379',
        '_gid': 'GA1.2.1579947978.1622734379',
        'clientId': '1575819242.1622734379',
        'ekConsentTcf2': '{%22customVersion%22:2%2C%22encodedConsentString%22:%22CPHOZ3KPHOZ3KE1ABADEBQCgAP_AAAAAAAYgHhNf_X_fb3_j-_59__t0eY1f9_7_v-0zjhfds-8N2f_X_L8X_2M7vF36pr4KuR4ku3bBIQdtHOncTUmx6olVrTPsbk2Mr7NKJ7Pkmnsbe2dYGH9_n93T_ZKZ7__v___7________7_______3_v_____-_____9___8AAABISADAAEDwg0AGAAIHhCIAMAAQPCFQAYAAgeEMgAwABA8IdABgACB4RCADAAEDwiUAGAAIHhFIAMAAQPCA.YAAAAAAAASA%22%2C%22googleConsentGiven%22:true%2C%22consentInterpretation%22:{%22googleAdvertisingFeaturesAllowed%22:true}}',
        'ekConsentBucketTcf2': 'full2-exp',
        '__gads': 'ID=dd0634b32eb1c791-224f000156c8008c:T=1622741116:S=ALNI_MaHcLTHFB9U6gx4xkAu8SwGwBq-jQ',
        'overlayV21': 'seen',
        'wl': '%7B%22l%22%3A%22%22%7D',
        'sc': '%7B%7D',
        'POPUPCHECK': '1622820883139',
        'cto_bundle': 'zkMxmV9uUzRqZmlwTmVWT1k5ZEc3ZjB0ZHlOdGZxcDh2NU16Z2l3cVRqc0VsJTJGUUhWN29FajVMWjdZb3ZYY3dOMGluZkw5WUdIdkV6SCUyRlBvUU9yWU5WUXZYbjVuSXZDcCUyRnZNZ0VydER6cWJsY3BSQWdqZVFjUkFwbzQ0MGJJSVRVYkl6R0Q3dmR4THBmR0VKVjkyJTJGTHFkUG1zYkFJYXFDNjZxak1XNEFSWGs5SEUyJTJGZ1dBQ2xZejhWeXFFN1JidUNRSkRLQ25iazExVGxiVlFFemNJVmtrVzZZdyUzRCUzRA',
        '_gat': '1',
        'JSESSIONID': 'EA9B063144FBBF1CDDBF5EF4C4B04120-mc6.koeb47-22_i01_1001',
    }


data = {
    'targetUrl': '/',
    #'loginWenkseSessionId': '19432925-f84f-49ca-9a47-9317544d2a62',
    'loginMail': 'emin.sofi2016@gmail.com',
    'password': 'emin.sofi12',
  #  '_csrf': '01d47efe-bf85-42e6-82d0-2f4a516a907e',
   # 'fingerprint': 'befd0bc4388a80ed7daa1d4ebe0bda00'
}

headers_dm = {
    'Host': 'gateway.ebay-kleinanzeigen.de',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'application/json',
    'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://www.ebay-kleinanzeigen.de/',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI3NjQxODYyNSIsImVtYWlsIjoiZS5zb2ZpMjAxNkBnbWFpbC5jb20iLCJleHAiOjE2MjI3OTIyNzR9.-T7gAPd6w4HVmi_6gjqV0p2ucj8asJ_v0mTZxYjEtfZz4DRD8StAku2wgcvrc7GWunUA6ZdHvts9MXaCB8O3ug',
    'Content-Type': 'application/json',
    'Origin': 'https://www.ebay-kleinanzeigen.de',
    'Content-Length': '30',
    'Te': 'trailers',
    'Connection': 'close',
}
cookies_dm = {
    'ioam2018': '0014660c08673577a60b8f62a:1653579178191:1622734378191:.ebay-kleinanzeigen.de:19:ebaykanz:ebayK-8:noevent:1622790472671:6ymn6l',
    'iom_consent': '0103ff03ff&1622734382291',
    '_ga': 'GA1.2.1575819242.1622734379',
    '_gid': 'GA1.2.1579947978.1622734379',
    'ekConsentTcf2': '{%22customVersion%22:2%2C%22encodedConsentString%22:%22CPHOZ3KPHOZ3KE1ABADEBQCgAP_AAAAAAAYgHhNf_X_fb3_j-_59__t0eY1f9_7_v-0zjhfds-8N2f_X_L8X_2M7vF36pr4KuR4ku3bBIQdtHOncTUmx6olVrTPsbk2Mr7NKJ7Pkmnsbe2dYGH9_n93T_ZKZ7__v___7________7_______3_v_____-_____9___8AAABISADAAEDwg0AGAAIHhCIAMAAQPCFQAYAAgeEMgAwABA8IdABgACB4RCADAAEDwiUAGAAIHhFIAMAAQPCA.YAAAAAAAASA%22%2C%22googleConsentGiven%22:true%2C%22consentInterpretation%22:{%22googleAdvertisingFeaturesAllowed%22:true}}',
    'ekConsentBucketTcf2': 'full2-exp',
    '__gads': 'ID=dd0634b32eb1c791:T=1622741218:S=ALNI_MYfCFVhfGmH4p4I3iZ-UDzaMnhywA',
    'cto_bundle': 'MgrNU19uUzRqZmlwTmVWT1k5ZEc3ZjB0ZHlCcUc5MWYlMkI4dG1PNW55WnJVOTVkNFMxWHlpNlJvY1lDdWJnQzRiUSUyQnlMYlBva2hiUUJXb2ZGaXhOR2xMT295Tm5tJTJGaWVwOTVIUTBUeDAwSnBKZ21xaXZPa2UxUE9tWkNpRU5OTE80ZE1SN2k4RGxpdGhQYlZPUDkwSXd0VDEyajRmdFVIMTRPUWloVXNUQVMlMkJnUXR6QTd4ZTVSSWNQWkg1dnQ1MnkyTlZsUm8xNEh2dkZybkJDZmE0dGNrSzJ3MWclM0QlM0Q',
    'rbzid': 'A4tF5CwJBAdcRyPsNPgk9MBkZXRpMBvI5KQ3yGQfnP4yOb6GR1gGAPOn0JMV691skrQXbXoBBiKmIS30t2CSn4dKdgeQXBdrBlAxbq3WwgGTFr1FdNNVKWuthWlcijL/YuIVIWbMKz4E6RwRnE6ZyNSuBjY+p+uOher9tsPH3srSZynLtsXgicQQcGEHdyqrfI9BHZ7+AWvVvvMulUmPvg==',
    'rbzsessionid': 'd9e7381f978b1515c7e5bc426750fbf7',
    '_gat': '1',
    'route_d6bfec5b_c9f3_4715_b3e6_f05b02bf3b58': '6e454b6830c4cd3a1893c012d9ac2a82',
    'GCLB': 'CJnXxLmnmIuC2AE',
}
with requests.Session() as s:
    response = s.get('https://www.ebay-kleinanzeigen.de/', headers=headers)# cookies=cookies)
    response_login = s.post('https://www.ebay-kleinanzeigen.de/m-einloggen.html', data=data)# headers=login_headers(csrf_token), cookies=cookies_login,)
    print(response_login.status_code)
    print(response_login.content)




    data_dm = '{"message":"Was letzte Preis"}'

    #response = requests.post('https://gateway.ebay-kleinanzeigen.de/messagebox/api/users/76418625/conversations/bq58:fcv7km:2g497g1xg', headers=headers_dm, cookies=cookies_dm, data=data_dm)