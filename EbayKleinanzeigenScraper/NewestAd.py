from lxml import html
import requests
from lxml.etree import tostring
from EbayKleinanzeigenScraper.EbayKleinanzeigenScraper import EbayKleinanzeigenScraper
from advertisement import Advertisement, EmptyAdClass
import random
import time


class NewestAd(EbayKleinanzeigenScraper):

    def __init__(self, search, region=None, min_price=None, max_price=None, category=None, anzeige=None, radius=0,
                 condition=None, delivery=None):
        super().__init__(search, region, min_price, max_price, category, anzeige, radius, condition, delivery)
        self.kill_switch = False
        self.newest_ad = EmptyAdClass()


    def check_newest_ad(self):

        response = requests.get(self.url + "/s-suchanfrage.html", headers=self.headers, params=self.parameters)
        content = response.content
        parser = html.fromstring(content)
        page_ads = parser.xpath('//*[@id="srchrslt-adtable"]/li')
        cur_ad = self.get_first_ad(page_ads)
        #if cur_ad == False:
         #   return EmptyAdClass()
        cur_title = cur_ad.xpath('div[2]/div[2]/h2/a/text()')[0]
        cur_selling_location = cur_ad.xpath('div[2]/div[1]/div[1]/text()')[1].strip()
        #print(cur_selling_location)
        cur_selling_date = str(cur_ad.xpath('div[2]/div[1]/div[2]/text()')[1].strip())
        #print(cur_selling_date)
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


        #time.sleep(random.uniform(45.0, 60.0))

        return Advertisement(url=cur_url, title=cur_title, date=cur_selling_date,
                                   location=cur_selling_location, delivery=None, condition=None,
                                   price=cur_price,
                                   thumbnail=cur_thumbnail)

    def get_first_ad(self, ads: list):
        for ad in ads:
            if ad.xpath('@class')[0].strip() == "ad-listitem lazyload-item":
                return ad.xpath('article')[0]
        else:
            return False

    def get_var_newest_ad(self):
        return self.newest_ad

    def set_var_newest_ad(self, args):
        self.newest_ad = args

    def get_kill_switch(self):
        return self.kill_switch

    def set_kill_switch(self, kill_switch_bool: bool):
        self.kill_switch = kill_switch_bool
