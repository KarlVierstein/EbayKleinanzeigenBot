from lxml import html
import requests
from lxml.etree import tostring
from EbayKleinanzeigenScraper.EbayKleinanzeigenScraper import EbayKleinanzeigenScraper
from advertisement import Advertisement, EmptyAdClass
import random
import time
from EbayKleinanzeigenScraper.ExtractAd import exctract_from_ad



class AdListener(EbayKleinanzeigenScraper):

    def __init__(self, search, region=None, min_price=None, max_price=None, category=None, anzeige=None, radius=0,
                 condition=None, delivery=None):
        super().__init__(search, region, min_price, max_price, category, anzeige, radius, condition, delivery)
        self.kill_switch = False
        self.newest_ad = Advertisement(url=" ", title="", date=" ",
                             location=" ", delivery=None, condition=None,
                             price=" ", thumbnail=" ")


    def listen_on_ad(self):
        response = requests.get(self.url + "/s-suchanfrage.html", headers=self.headers, params=self.parameters)
        content = response.content
        parser = html.fromstring(content)
        page_ads = parser.xpath('//*[@id="srchrslt-adtable"]/li')
        cur_ad = self.get_first_ad(page_ads)
        if cur_ad == False:
            return EmptyAdClass()

        cur_ad = exctract_from_ad(cur_ad)

        self.set_var_newest_ad(cur_ad)

        return cur_ad

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
