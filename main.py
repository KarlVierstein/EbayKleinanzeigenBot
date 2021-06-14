from EbayKleinanzeigenScraper.EbayKleinanzeigenScraper import EbayKleinanzeigenScraper
from EbayKleinanzeigenScraper.AdListener import AdListener
from Threads.myTreads import getCurAdThread, myListenerThread, getAds
"""
bot = EbayKleinanzeigenScraper("iPhone")
items, max_ads = bot.get_first_page()
items2 = bot.get_other_pages(bot.get_max_pages(max_ads), 2)

ads = items + items2
for item in ads:
    print(item.price + " " + item.url)

print(len(ads))
"""
bot1 = AdListener("iPhone")
bot2 = EbayKleinanzeigenScraper("iPhone", region="Berlin")
#"""
thread1 = myListenerThread(1, "Thread-1", bot1)
thread2 = getCurAdThread(2, "Thread-2", bot1)
thread3 = getAds(2, "Thread-3", bot2)

# Start new Threads
thread1.start()
thread2.start()
#thread3.start()

#print(thread3.join())