from EbayKleinanzeigenScraper.EbayKleinanzeigenScraper import EbayKleinanzeigenScraper
from EbayKleinanzeigenScraper.NewestAd import NewestAd

"""
bot = EbayKleinanzeigenScraper("iPhone")
items, max_ads = bot.get_first_page()
items2 = bot.get_other_pages(bot.get_max_pages(max_ads), 2)

ads = items + items2
for item in ads:
    print(item.price + " " + item.url)

print(len(ads))
"""
bot = NewestAd("iPhone")
latest_ad = bot.check_newest_ad()
print(latest_ad.url)
print(latest_ad.thumbnail)
print(latest_ad.date)
print(latest_ad.location)
bot.set_kill_switch(True)
#"""