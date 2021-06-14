import threading
import time


class myListenerThread(threading.Thread):
    def __init__(self, threadID, name, bot):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.bot = bot

    def run(self):
        print("Starting " + self.name)
        latest_ad = self.bot.listen_on_ad()
        print("Exiting " + self.name)


class getCurAdThread(threading.Thread):
    def __init__(self, threadID, name, bot):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.bot = bot
        self._return = None

    def run(self):
        print("Starting " + self.name)
        time.sleep(10)
        print(self.bot.newest_ad.url)
        print(self.bot.newest_ad.date)
        print(self.bot.newest_ad.thumbnail)
        self._return = self.bot.newest_ad
        print("Exiting " + self.name)

    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return

class getAds(threading.Thread):
    def __init__(self, threadID, name, bot):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.bot = bot
        self._return = None

    def run(self):
        print("Starting " + self.name)
        items, max_ads = self.bot.get_first_page()
        items2 = self.bot.get_other_pages(self.bot.get_max_pages(max_ads), 2)

        items = items + items2
        self._return = items
        print("Exiting " + self.name)

    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return