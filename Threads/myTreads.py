import threading
import time
from advertisement import EmptyAdClass


class myListenerThread(threading.Thread):
    def __init__(self, threadID, name, bot):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.bot = bot
        self._return = EmptyAdClass()

    def run(self):
        print("Starting " + self.name)
        latest_ad = self.bot.listen_on_ad()
        self._return = latest_ad
        print("Exiting " + self.name)

    def return_element(self, *args):
        threading.Thread.join(self, *args)
        return self._return



class getAds(threading.Thread):
    def __init__(self, threadID, name, bot):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.bot = bot
        self._return = EmptyAdClass()

    def run(self):
        print("Starting " + self.name)
        items, max_ads = self.bot.get_first_page()
        items2 = self.bot.get_other_pages(self.bot.get_max_pages(max_ads), 2)

        items = items + items2
        self._return = items
        print("Exiting " + self.name)

    def return_element(self, *args):
        threading.Thread.join(self, *args)
        return self._return