import pytz
import requests
from lxml import html
import random
import time
import math
from datetime import datetime, timedelta
from advertisement import Advertisement

from lxml.etree import tostring


class EbayKleinanzeigenScraper:
    def __init__(self, search, region=None, min_price=None, max_price=None, category=None, anzeige=None, radius=0,
                 condition=None, delivery=None):
        self.search = search
        self.region = region
        self.radius = radius
        self.min_price = min_price
        self.max_price = max_price
        self.category = category
        self.ad_type = anzeige
        self.url = f"https://www.ebay-kleinanzeigen.de"
        self.url_tribe = ""
        self.condition = condition
        self.delivery = delivery
        self.parameters = (
            ('keywords', self.search),
            ('categoryId', ''),
            ('locationStr', self.region),  # 16761
            ('locationId', ''),
            ('radius', self.radius),
            ('sortingField', 'SORTING_DATE'),
            ('adType', self.ad_type),  # WANTED=Gesuche or OFFER=Angebot
            ('posterType', ''),  #COMMERCIAL=Gewerblich or PRIVATE=Privat
            ('pageNum', ''),
            ('action', 'find'),  # find
            ('maxPrice', self.max_price),
            ('minPrice', self.min_price),
            ('condition_s', self.condition),    # condition_used=Gebraucht &&& condition_new=Neu &&& condition_faulty=Defekt
            ('versand_s', self.delivery),  # ja or nein
        )

        self.user_agents = [
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

        self.headers = {
            'Host': 'www.ebay-kleinanzeigen.de',
            'Sec-Ch-Ua-Mobile': '?0',
            #    'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.user_agents[random.randint(0, len(self.user_agents) - 1)],
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            #    'Sec-Fetch-Site': 'same-origin',
            #   'Sec-Fetch-Mode': 'navigate',
            #  'Sec-Fetch-User': '?1',
            # 'Sec-Fetch-Dest': 'document',
            # 'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'Connection': 'close',
        }

    def get_first_page(self):
        content = requests.get(self.url + "/s-suchanfrage.html", headers=self.headers, params=self.parameters).content
        parser = html.fromstring(content)
        ads = []
        page_content = parser.xpath('//*[@id="srchrslt-adtable"]/li/article')
        max_ads = parser.xpath('//*[@id="srchrslt-content"]/div[3]/div[1]/div[1]/div[1]/span/strong[1]/text()')
        if max_ads == None or max_ads < 28:
            max_ads = 0
        else:
            max_ads = int(parser.xpath('//*[@id="srchrslt-content"]/div[3]/div[1]/div[1]/div[1]/span/strong[1]/text()')[0])
        # cur_page = parser.xpath('//*[@id="srchrslt-pagination"]/div/div[1]/span[1]/text()')[0]
        # max_sites = self.get_max_pages(max_ads)
            self.set_url_tribe(parser)

            for i in range(len(page_content)):
                element = page_content[i]
                title = element.xpath('div[2]/div[2]/h2/a/text()')[0]
                selling_location = element.xpath('div[2]/div[1]/div[1]/text()')
                selling_date = str(element.xpath('div[2]/div[1]/div[2]/text()')[1].strip())
                if selling_date[0:5] == "Heute":
                    selling_date = selling_date[:0] + self.get_date() + selling_date[5:]
                elif selling_date[0:7] == "Gestern":
                    selling_date = selling_date[:0] + self.get_date_tmrw() + selling_date[7:]
                url = "https://ebay-kleinanzeigen.de" + element.xpath('@data-href')[0]
                thumbnail = element.xpath('div[1]/a/div/@data-imgsrc')
                if len(thumbnail) == 0:
                    thumbnail.append("https://www.happypostcards.de/img/p/de-default-big_default.jpg")

                price = element.xpath('div[2]/div[2]/p[2]/text()')[0].strip()
                ad = Advertisement(url=url, title=title, date=selling_date, location=selling_location, delivery=None,
                                   condition=None, price=price, thumbnail=thumbnail[0])

                ads.append(ad)

        return ads, max_ads

    def get_other_pages(self, last_page: int, max_page_until_run):
        ads_other_sites = []
        for i in range(max_page_until_run):
            self.change_site_url_tribe(i + 2)
            content = requests.get(self.url + self.get_url_tribe(), headers=self.headers).content
            parser = html.fromstring(content)
            page_content = parser.xpath('//*[@id="srchrslt-adtable"]/li/article')

            for j in range(len(page_content)):
                element = page_content[j]

                title = element.xpath('div[2]/div[2]/h2/a/text()')[0]
                selling_location = element.xpath('div[2]/div[1]/div[1]/text()')
                selling_date = str(element.xpath('div[2]/div[1]/div[2]/text()')[1].strip())
                thumbnail = element.xpath('div[1]/a/div/@data-imgsrc')
                if len(thumbnail) == 0:
                    thumbnail.append("https://www.happypostcards.de/img/p/de-default-big_default.jpg")
                if selling_date[0:5] == "Heute":
                    selling_date = selling_date[:0] + self.get_date() + selling_date[5:]
                elif selling_date[0:7] == "Gestern":
                    selling_date = selling_date[:0] + self.get_date_tmrw() + selling_date[7:]
                url = "https://ebay-kleinanzeigen.de" + element.xpath('@data-href')[0]
                price = element.xpath('div[2]/div[2]/p[2]/text()')[0].strip()
                ad = Advertisement(url=url, title=title, date=selling_date, location=selling_location, delivery=None,
                                   condition=None, price=price, thumbnail=thumbnail[0])

                ads_other_sites.append(ad)
        self.short_pause()
        return ads_other_sites

    def set_url_tribe(self, parser=None, new_text=None):
        if new_text is not None:
            self.url_tribe = new_text
        elif parser is not None:
            next_page_button = parser.xpath('//*[@id="srchrslt-pagination"]/div/div[2]/a/@href')[0]
            self.url_tribe = next_page_button

    def get_url_tribe(self):
        return self.url_tribe

    def change_site_url_tribe(self, page_num):
        finding_word = "seite:"
        start_index = self.get_url_tribe().find(finding_word)
        end_index = start_index + len(finding_word)
        if 10 <= page_num < 100:
            self.set_url_tribe(
                new_text=self.get_url_tribe()[:end_index] + f"{str(page_num)}" + self.get_url_tribe()[end_index + 2:])
        elif 100 <= page_num < 1000:
            self.set_url_tribe(
                new_text=self.get_url_tribe()[:end_index] + f"{str(page_num)}" + self.get_url_tribe()[end_index + 3:])
        elif 1000 <= page_num < 10000:
            self.set_url_tribe(
                new_text=self.get_url_tribe()[:end_index] + f"{str(page_num)}" + self.get_url_tribe()[end_index + 4:])
        else:
            self.set_url_tribe(
                new_text=self.get_url_tribe()[:end_index] + f"{str(page_num)}" + self.get_url_tribe()[end_index + 1:])
        print(self.get_url_tribe())

    def get_url(self):
        return self.url

    def set_url(self, new_url):
        self.url = new_url

    def short_pause(self):
        print(random.uniform(0.1, 2.0))
        time.sleep(random.uniform(0.1, 2.0))

    def long_pause(self):
        pass

    def check_newest_ad(self):
        newest_ad = Advertisement(url=None, title=None, date=None, location=None, delivery=None,condition=None, price=None, thumbnail=None)

        while True:
            content = requests.get(self.url + self.get_url_tribe(), headers=self.headers).content
            parser = html.fromstring(content)
            cur_ad = parser.xpath('//*[@id="srchrslt-adtable"]/li/article')[0]
            cur_title = cur_ad.xpath('div[2]/div[2]/h2/a/text()')[0]
            cur_selling_location = cur_ad.xpath('div[2]/div[1]/div[1]/text()')
            cur_selling_date = str(cur_ad.xpath('div[2]/div[1]/div[2]/text()')[1].strip())
            if cur_ad.xpath('div[1]/a/div/@class') == "imagebox srpimagebox is-nopic":
                cur_thumbnail = "https://www.happypostcards.de/img/p/de-default-big_default.jpg"
            else:
                cur_thumbnail = cur_ad.xpath('div[1]/a/div/@data-imgsrc')[0]
            if cur_selling_date[0:5] == "Heute":
                cur_selling_date = cur_selling_date[:0] + self.get_date() + cur_selling_date[5:]
            elif cur_selling_date[0:7] == "Gestern":
                cur_selling_date = cur_selling_date[:0] + self.get_date_tmrw() + cur_selling_date[7:]
            cur_url = "https://ebay-kleinanzeigen.de" + cur_ad.xpath('@data-href')[0]
            # print(tostring(element))
            cur_price = cur_ad.xpath('div[2]/div[2]/p[2]/text()')[0].strip()

            cur_ad_obj = Advertisement(url=cur_url, title=cur_title, date=cur_selling_date, location=cur_selling_location, delivery=None,condition=None, price=cur_price, thumbnail=cur_thumbnail)

            if newest_ad.url != cur_ad.url:
                newest_ad = cur_ad_obj

            time.sleep(random.uniform(45.0, 60.0))

    def get_max_pages(self, max_elements):
        return math.ceil(max_elements / 27)

    def get_date(self):
        return str(datetime.now(pytz.timezone('Europe/Berlin')).strftime('%d.%m.%Y'))

    def get_date_tmrw(self):
        return str((datetime.utcnow().date() - timedelta(days=1)).strftime('%d.%m.%Y'))

    def get_ad_type(self):
        return self.ad_type

bot = EbayKleinanzeigenScraper("Manga", anzeige="OFFER")
items, max_ads = bot.get_first_page()
items2 = bot.get_other_pages(bot.get_max_pages(max_ads), 2)

ads = items + items2
for item in ads:
    print(item.price + " " + item.url)

print(len(ads))

