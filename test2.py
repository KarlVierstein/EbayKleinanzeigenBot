import requests
from lxml import html
from lxml.etree import tostring
import itertools
import math
import time
import random
import urllib

url = "https://www.ebay-kleinanzeigen.de/s-suchanfrage.html"
page_num = 1
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
]
anzeigen = set()
cookies = {
    '$_ga': 'GA1.2.291931199.1622214046',
    'clientId': '291931199.1622214046',
    'ekConsentBucketTcf2': 'full2-exp',
    'iom_consent': '0103ff03ff&1622214078090',
    'ekConsentTcf2': '{%22customVersion%22:2%2C%22encodedConsentString%22:%22CPG6jl3PG6jl3E1ABADEBQCgAP_AAAAAAAYgHhNf_X_fb3_j-_59__t0eY1f9_7_v-0zjhfds-8N2f_X_L8X_2M7vF36pr4KuR4ku3bBIQdtHOncTUmx6olVrTPsbk2Mr7NKJ7Pkmnsbe2dYGH9_n93T_ZKZ7__v___7________7_______3_v_____-_____9___8AAABJSADAAEDwiUAGAAIHhEIAMAAQPCHQAYAAgeEMgAwABA8IVABgACB4QiADAAEDwg0AGAAIHhBIAMAAQPCA.YAAAAAAAASA%22%2C%22googleConsentGiven%22:true%2C%22consentInterpretation%22:{%22googleAdvertisingFeaturesAllowed%22:true}}',
    'overlayV21': 'seen',
    '__gads': 'ID=e8a0da3eb3714af0:T=1622214079:S=ALNI_MYjmTkl69U4L1qA3yqsPDpkQtognw',
    'uh': '%7B%22sh%22%3A%22k%3Diphone%25208%3A%3Ak%3Diphone%25207%3A%3Ak%3Diphone%22%7D',
    'CSRF-TOKEN': '1af8446f-2f8c-4d8a-9f15-e010accd73b0',
    'up': '%7B%22ln%22%3A%22473390967%22%2C%22lln%22%3A%22f8a25dd7-a579-41be-b9bb-43b9251ccd0b%22%2C%22llstv%22%3A%2297-js-errorlog%3DA%7CBLN-18532_highlight%3DB%7CBLN-18275-lazy-load-image%3DA%7CDesktop_Test%3DA%7Creact-msgbox-payment-buy%3DB%7Creact-msgbox-payship%3DB%7CBLN-18685_auth_svr%3DA%7Cspeedcurve-labs-lux-1%3DA%7Cgdpr-experimental%3DB%7Cspeedcurve-labs-lux-2%3DA%7CBLN-18221_srp_rebrush_ads%3DB%7CBLN-18849-manage-ads-k8s%3DB%7C76-preact-header-footer%3DA%7CBLN-18727-TopAd-enabler%3DA%7C74-react-messagebox%3DA%7CEBAYKAD-2252_group-assign%3DB%22%2C%22ls%22%3A%22k%3Diphone%25208%22%2C%22va%22%3A%221780565842%22%2C%22vapwrncats%22%3A1%7D',
    'GCLB': 'CKXdurmUrujv7QE',
    '_gid': 'GA1.2.2116457354.1622316307',
    'POPUPCHECK': '1622402708106',
    'ioam2018': '000ed90b73261135360b1059d:1648220446343:1622214046344:.ebay-kleinanzeigen.de:18:ebaykanz:ebayK-2:noevent:1622316378785:i04v4',
}

headers = {
    'Host': 'www.ebay-kleinanzeigen.de',
    #    'Sec-Ch-Ua-Mobile': '?0',
    #    'Upgrade-Insecure-Requests': '1',
    'User-Agent': user_agents[random.randint(0, len(user_agents) - 1)],
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #    'Sec-Fetch-Site': 'same-origin',
    #   'Sec-Fetch-Mode': 'navigate',
    #  'Sec-Fetch-User': '?1',
    # 'Sec-Fetch-Dest': 'document',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Connection': 'close',
}

params = (
    ('keywords', 'iphone'),
    ('categoryId', ''),
    ('locationStr', ''),  # 16761
    ('locationId', ''),
    ('radius', ''),
    ('sortingField', 'SORTING_DATE'),
    ('adType', 'OFFER'),  # WANTED=Gesuche or OFFER=Angebot
    ('posterType', ''),
    ('pageNum', ''),
    ('action', 'find'),  # find
    ('maxPrice', ''),
    ('minPrice', ''),
    # ('condition_s', ''),        #condition_used=Gebraucht &&& condition_new=Neu &&& condition_faulty=Defekt
    # ('versand_s', ''),                        #ja=Versand möglich  &&& nein=Nur Abholung
)


def set_url(new_url):
    url = new_url


def get_next_page_link(parser, max_page):
    more_pages = parser.xpath('//*[@id="srchrslt-pagination"]/div/div[1]')
    cur_page = parser.xpath('//*[@id="srchrslt-pagination"]/div/div[1]/span/text()')[0]
    if cur_page == max_page:
        return
    else:
        next_page_num = int(cur_page) + 1
        next_page = \
        parser.xpath(f'//*[@id="srchrslt-pagination"]/div/div[1]/a[contains(text(),"{str(next_page_num)}")]')[0]
        next_page_link = next_page.xpath('@href')[0]
        return next_page_link


while page_num < 3:
    response = requests.get('https://www.ebay-kleinanzeigen.de/s-suchanfrage.html', headers=headers, params=params)
    print("Page: " + str(page_num))
    parser = html.fromstring(response.content)
    page_content = parser.xpath('//*[@id="srchrslt-adtable"]/li/article')
    max_elements = int(parser.xpath('//*[@id="srchrslt-content"]/div[3]/div[1]/div[1]/div[1]/span/strong[1]/text()')[0])
    cur_page = parser.xpath('//*[@id="srchrslt-pagination"]/div/div[1]/span[1]/text()')[0]
    print(cur_page)
    max_sites = math.ceil(max_elements / 27)
    print(max_elements)
    next_page_link = get_next_page_link(parser, max_sites)
    print(next_page_link)
    # print(tostring(more_pages[i]))

    for i in range(len(page_content)):
        element = page_content[i]
        title = element.xpath('div[2]/div[2]/h2/a/text()')[0]
        link = element.xpath('@data-href')[0]
        url = "https://ebay-kleinanzeigen.de" + link
        # print(tostring(element))
        price = element.xpath('div[2]/div[2]/p[2]/text()')[0].strip()
        # print(title + " " + price + " " + url)
        anzeigen.add(title + " " + price + " " + url)

    page_num += 1
    time.sleep(2)

print(len(anzeigen))

# print(price.strip() + " | " + title + " | " + url)

# response = requests.get('$https://www.ebay-kleinanzeigen.de/s-suchanfrage.html?keywords=iphone+8&categoryId=&locationStr=16761&locationId=&radius=0&sortingField=SORTING_DATE&adType=&posterType=&pageNum=1&action=find&maxPrice=&minPrice=', headers=headers, cookies=cookies, verify=False)
