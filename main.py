from EbayKleinanzeigenScraper.EbayKleinanzeigenScraper import EbayKleinanzeigenScraper
from EbayKleinanzeigenScraper.AdListener import AdListener
from Threads.myTreads import myListenerThread, getAds
from PriceCalc.Method1 import CalculateMethod
from utils import clean_prices

"""
bot = EbayKleinanzeigenScraper("iPhone")
items, max_ads = bot.get_first_page()
items2 = bot.get_other_pages(bot.get_max_pages(max_ads), 2)

ads = items + items2
for item in ads:
    print(item.price + " " + item.url)

print(len(ads))
"""
bot1 = AdListener("iPhone 12 Pro", region="Berlin", min_price="200")
bot2 = EbayKleinanzeigenScraper("iPhone 12 Pro", region="Berlin", min_price="200")

thread1 = myListenerThread(1, "Thread-1", bot1)
thread2 = getAds(2, "Thread-2", bot2)

# Start new Threads
thread1.start()
thread2.start()

latest_ad = thread1.return_element()
items = thread2.return_element()

prices = clean_prices.filter_prices(items)
opt_price = CalculateMethod.calc_optimum_price(prices)
print(opt_price)
print(latest_ad.date)
# print(len(price_elements))
"""
bot = AdListener("iPhone", region="Berlin", min_price="200")
latest_ad = bot.listen_on_ad()
"""