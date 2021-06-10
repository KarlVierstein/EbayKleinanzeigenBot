"""
import requests

# up, sc, JSESSIONID, wl

cookies = {
    'ioam2018': '0014660c08673577a60b8f62a:1653579178191:1622734378191:.ebay-kleinanzeigen.de:27:ebaykanz:ebayK-6:noevent:1622822548077:3vhccz',
    'iom_consent': '0103ff03ff&1622734382291',
    '_ga': 'GA1.2.1575819242.1622734379',
    '_gid': 'GA1.2.1579947978.1622734379',
    'clientId': '1575819242.1622734379',
    'ekConsentTcf2': '{%22customVersion%22:2%2C%22encodedConsentString%22:%22CPHOZ3KPHOZ3KE1ABADEBQCgAP_AAAAAAAYgHhNf_X_fb3_j-_59__t0eY1f9_7_v-0zjhfds-8N2f_X_L8X_2M7vF36pr4KuR4ku3bBIQdtHOncTUmx6olVrTPsbk2Mr7NKJ7Pkmnsbe2dYGH9_n93T_ZKZ7__v___7________7_______3_v_____-_____9___8AAABISADAAEDwg0AGAAIHhCIAMAAQPCFQAYAAgeEMgAwABA8IdABgACB4RCADAAEDwiUAGAAIHhFIAMAAQPCA.YAAAAAAAASA%22%2C%22googleConsentGiven%22:true%2C%22consentInterpretation%22:{%22googleAdvertisingFeaturesAllowed%22:true}}',
    'ekConsentBucketTcf2': 'full2-exp',
    '__gads': 'ID=dd0634b32eb1c791-22c4a00056c800a4:T=1622822550:S=ALNI_MZ_-IJjA6SBa1miTpXwKdFdurEHHA',
    'overlayV21': 'seen',
    'wl': '%7B%22l%22%3A%22%22%7D',
    'cto_bundle': 'wfk--F9uUzRqZmlwTmVWT1k5ZEc3ZjB0ZHlFRlF0NGtOS2FnWlpKTk9lUk1LNVlqREtCOCUyQm91VCUyRmxXJTJCU1hqRTF4dCUyRmFFZXVtN0pTTzNEQWV5c3RkRElpVkxhZDNUWXR2Ukhid1YweExlbiUyQnd1aXdwelJOTEZ0amRGR0hENkxPZjJOeTlpbDlnQWI1SXVxdHgyR1AyeTNGekZwNzA5bkdtTTY5RUpScXpQMFgyT2x5RlNXWDhKMmxHdkVRdWV1WU1oWjdwQk9VUmVkZE9TNDJGVHA0cWIxTG1xUSUzRCUzRA',
    'CSRF-TOKEN': 'c41e3601-f3dc-4c3b-8882-dc5414fad434',
    'GCLB': 'CKfHzPj_0JyyZg',
    'rbzid': '6Zd+zfSs390l0PQBftBLwBZlGONQE1Q7rW06JmlG/8whWfM15+QrOU9A+5eVsW9pg374daa1KnZkHAn5QukKeSyH8R0AffHFdw4juvX+ib3xMxNYZsrXy+hoqoMfP9aBAaGhc5ZrAc0WYjo6JTetvv3zRRCa+K6LdPoE8kDP5BEQs8Ws+bhC7/SPkwcg8OQxEqOVligCVmQ29frIc3yUp/Wi73iPZjeRAo5h6+EZSBw=',
    'rbzsessionid': '2b1c387a48c1511e526273b7d16636a5',
    'sc': '%7B%7D',
    'POPUPCHECK': '1622908021883',
    '_gat': '1',
    'JSESSIONID': '4FB5F2E03A7F72F5EC881ADB82B68DFE-mc1.ebayk-worker029-dus1',
}

headers = {
    'Host': 'www.ebay-kleinanzeigen.de',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '210',
    'Origin': 'https://www.ebay-kleinanzeigen.de',
    'Referer': 'https://www.ebay-kleinanzeigen.de/m-einloggen.html',
    'Upgrade-Insecure-Requests': '1',
    'Te': 'trailers',
    'Connection': 'close',
}

data = 'targetUrl=&loginWenkseSessionId=463d85fb-bbde-4f1b-9a21-2e4e81780e33&loginMail=e.sofi2016%40gmail.com&password=emin.sofi12&_csrf=c41e3601-f3dc-4c3b-8882-dc5414fad434&fingerprint=f25bd96dc7d5816abaec41a990563f02'
data_short = 'loginMail=e.sofi2016%40gmail.com&password=emin.sofi12&_csrf=c41e3601-f3dc-4c3b-8882-dc5414fad434'


response = requests.post('https://www.ebay-kleinanzeigen.de/m-einloggen.html', headers=headers, data=data)

response_cookies = response.headers
print(response_cookies)

"""
import requests

session = requests.session()

burp0_url = "https://www.ebay-kleinanzeigen.de:443/m-einloggen.html?targetUrl=/m-meine-anzeigen.html&sessionExpired=true"

burp0_cookies = {
                #"up": "%7B%22ln%22%3A%22606300982%22%2C%22lln%22%3A%229300df05-6423-4cce-b3e8-22e4cbd650d7%22%2C%22llstv%22%3A%2297-js-errorlog%3DA%7CBLN-18532_highlight%3DB%7CBLN-18275-lazy-load-image%3DA%7CDesktop_Test%3DB%7Creact-msgbox-payment-buy%3DB%7Creact-msgbox-payship%3DB%7CBLN-18685_auth_svr%3DA%7Cspeedcurve-labs-lux-1%3DB%7Cgdpr-experimental%3DC%7Cspeedcurve-labs-lux-2%3DB%7CBLN-18221_srp_rebrush_ads%3DB%7CBLN-18849-manage-ads-k8s%3DB%7C76-preact-header-footer%3DA%7CBLN-18727-TopAd-enabler%3DA%7C74-react-messagebox%3DA%7CEBAYKAD-2252_group-assign%3DA%22%2C%22ls%22%3A%22l%3D0%22%2C%22saSe%22%3A%22%22%7D",
                 "ioam2018": "0014660c08673577a60b8f62a:1653579178191:1622734378191:.ebay-kleinanzeigen.de:27:ebaykanz:ebayK-6:noevent:1622822548077:3vhccz",
                 "iom_consent": "0103ff03ff&1622734382291",
                 "_ga": "GA1.2.1575819242.1622734379",
                 "_gid": "GA1.2.1579947978.1622734379",
                # "clientId": "1575819242.1622734379",
                 "ekConsentTcf2": "{%22customVersion%22:2%2C%22encodedConsentString%22:%22CPHOZ3KPHOZ3KE1ABADEBQCgAP_AAAAAAAYgHhNf_X_fb3_j-_59__t0eY1f9_7_v-0zjhfds-8N2f_X_L8X_2M7vF36pr4KuR4ku3bBIQdtHOncTUmx6olVrTPsbk2Mr7NKJ7Pkmnsbe2dYGH9_n93T_ZKZ7__v___7________7_______3_v_____-_____9___8AAABISADAAEDwg0AGAAIHhCIAMAAQPCFQAYAAgeEMgAwABA8IdABgACB4RCADAAEDwiUAGAAIHhFIAMAAQPCA.YAAAAAAAASA%22%2C%22googleConsentGiven%22:true%2C%22consentInterpretation%22:{%22googleAdvertisingFeaturesAllowed%22:true}}",
                 "ekConsentBucketTcf2": "full2-exp",
                 "__gads": "ID=dd0634b32eb1c791-22c4a00056c800a4:T=1622822550:S=ALNI_MZ_-IJjA6SBa1miTpXwKdFdurEHHA",
                 "overlayV21": "seen", "wl": "%7B%22l%22%3A%22%22%7D",
                 "cto_bundle": "wfk--F9uUzRqZmlwTmVWT1k5ZEc3ZjB0ZHlFRlF0NGtOS2FnWlpKTk9lUk1LNVlqREtCOCUyQm91VCUyRmxXJTJCU1hqRTF4dCUyRmFFZXVtN0pTTzNEQWV5c3RkRElpVkxhZDNUWXR2Ukhid1YweExlbiUyQnd1aXdwelJOTEZ0amRGR0hENkxPZjJOeTlpbDlnQWI1SXVxdHgyR1AyeTNGekZwNzA5bkdtTTY5RUpScXpQMFgyT2x5RlNXWDhKMmxHdkVRdWV1WU1oWjdwQk9VUmVkZE9TNDJGVHA0cWIxTG1xUSUzRCUzRA", "CSRF-TOKEN": "c41e3601-f3dc-4c3b-8882-dc5414fad434",
                 "GCLB": "CKfHzPj_0JyyZg", "rbzid": "6Zd+zfSs390l0PQBftBLwBZlGONQE1Q7rW06JmlG/8whWfM15+QrOU9A+5eVsW9pg374daa1KnZkHAn5QukKeSyH8R0AffHFdw4juvX+ib3xMxNYZsrXy+hoqoMfP9aBAaGhc5ZrAc0WYjo6JTetvv3zRRCa+K6LdPoE8kDP5BEQs8Ws+bhC7/SPkwcg8OQxEqOVligCVmQ29frIc3yUp/Wi73iPZjeRAo5h6+EZSBw=",
                 "rbzsessionid": "2b1c387a48c1511e526273b7d16636a5",
                 "sc": "%7B%7D",
                 "POPUPCHECK": "1622908021883",
                 "_gat": "1",
                "JSESSIONID": "4FB5F2E03A7F72F5EC881ADB82B68DFE-mc1.ebayk-worker029-dus1"
                 }

burp0_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "de,en-US;q=0.7,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Origin": "https://www.ebay-kleinanzeigen.de", "Referer": "https://www.ebay-kleinanzeigen.de/m-einloggen.html", "Upgrade-Insecure-Requests": "1", "Te": "trailers", "Connection": "close"}
response = session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

print(response.status_code)
res_headers = response.headers

burp0_url2 = "https://www.ebay-kleinanzeigen.de:443/m-einloggen.html"
burp0_cookies2 = {"up": "%7B%22ln%22%3A%22606300982%22%2C%22lln%22%3A%229300df05-6423-4cce-b3e8-22e4cbd650d7%22%2C%22llstv%22%3A%2297-js-errorlog%3DA%7CBLN-18532_highlight%3DB%7CBLN-18275-lazy-load-image%3DA%7CDesktop_Test%3DB%7Creact-msgbox-payment-buy%3DB%7Creact-msgbox-payship%3DB%7CBLN-18685_auth_svr%3DA%7Cspeedcurve-labs-lux-1%3DB%7Cgdpr-experimental%3DC%7Cspeedcurve-labs-lux-2%3DB%7CBLN-18221_srp_rebrush_ads%3DB%7CBLN-18849-manage-ads-k8s%3DB%7C76-preact-header-footer%3DA%7CBLN-18727-TopAd-enabler%3DA%7C74-react-messagebox%3DA%7CEBAYKAD-2252_group-assign%3DA%22%2C%22ls%22%3A%22l%3D0%22%2C%22saSe%22%3A%22%22%7D", "ioam2018": "0014660c08673577a60b8f62a:1653579178191:1622734378191:.ebay-kleinanzeigen.de:27:ebaykanz:ebayK-6:noevent:1622822548077:3vhccz", "iom_consent": "0103ff03ff&1622734382291", "_ga": "GA1.2.1575819242.1622734379", "_gid": "GA1.2.1579947978.1622734379", "clientId": "1575819242.1622734379", "ekConsentTcf2": "{%22customVersion%22:2%2C%22encodedConsentString%22:%22CPHOZ3KPHOZ3KE1ABADEBQCgAP_AAAAAAAYgHhNf_X_fb3_j-_59__t0eY1f9_7_v-0zjhfds-8N2f_X_L8X_2M7vF36pr4KuR4ku3bBIQdtHOncTUmx6olVrTPsbk2Mr7NKJ7Pkmnsbe2dYGH9_n93T_ZKZ7__v___7________7_______3_v_____-_____9___8AAABISADAAEDwg0AGAAIHhCIAMAAQPCFQAYAAgeEMgAwABA8IdABgACB4RCADAAEDwiUAGAAIHhFIAMAAQPCA.YAAAAAAAASA%22%2C%22googleConsentGiven%22:true%2C%22consentInterpretation%22:{%22googleAdvertisingFeaturesAllowed%22:true}}", "ekConsentBucketTcf2": "full2-exp", "__gads": "ID=dd0634b32eb1c791-22c4a00056c800a4:T=1622822550:S=ALNI_MZ_-IJjA6SBa1miTpXwKdFdurEHHA", "overlayV21": "seen", "wl": "%7B%22l%22%3A%22%22%7D", "cto_bundle": "wfk--F9uUzRqZmlwTmVWT1k5ZEc3ZjB0ZHlFRlF0NGtOS2FnWlpKTk9lUk1LNVlqREtCOCUyQm91VCUyRmxXJTJCU1hqRTF4dCUyRmFFZXVtN0pTTzNEQWV5c3RkRElpVkxhZDNUWXR2Ukhid1YweExlbiUyQnd1aXdwelJOTEZ0amRGR0hENkxPZjJOeTlpbDlnQWI1SXVxdHgyR1AyeTNGekZwNzA5bkdtTTY5RUpScXpQMFgyT2x5RlNXWDhKMmxHdkVRdWV1WU1oWjdwQk9VUmVkZE9TNDJGVHA0cWIxTG1xUSUzRCUzRA", "CSRF-TOKEN": "c41e3601-f3dc-4c3b-8882-dc5414fad434", "GCLB": "CKfHzPj_0JyyZg", "rbzid": "6Zd+zfSs390l0PQBftBLwBZlGONQE1Q7rW06JmlG/8whWfM15+QrOU9A+5eVsW9pg374daa1KnZkHAn5QukKeSyH8R0AffHFdw4juvX+ib3xMxNYZsrXy+hoqoMfP9aBAaGhc5ZrAc0WYjo6JTetvv3zRRCa+K6LdPoE8kDP5BEQs8Ws+bhC7/SPkwcg8OQxEqOVligCVmQ29frIc3yUp/Wi73iPZjeRAo5h6+EZSBw=", "rbzsessionid": "2b1c387a48c1511e526273b7d16636a5", "sc": "%7B%7D", "POPUPCHECK": "1622908021883", "_gat": "1", "JSESSIONID": "4FB5F2E03A7F72F5EC881ADB82B68DFE-mc1.ebayk-worker029-dus1"}
burp0_headers2 = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "de,en-US;q=0.7,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.ebay-kleinanzeigen.de", "Referer": "https://www.ebay-kleinanzeigen.de/m-einloggen.html", "Upgrade-Insecure-Requests": "1", "Te": "trailers", "Connection": "close"}
burp0_data = {"targetUrl": '', "loginWenkseSessionId": "463d85fb-bbde-4f1b-9a21-2e4e81780e33", "loginMail": "e.sofi2016@gmail.com", "password": "emin.sofi12", "_csrf": "c41e3601-f3dc-4c3b-8882-dc5414fad434", "fingerprint": "f25bd96dc7d5816abaec41a990563f02"}
res = session.post(burp0_url2, headers=burp0_headers2, cookies=burp0_cookies2, data=burp0_data)
print(res.status_code)
print(res.content)
