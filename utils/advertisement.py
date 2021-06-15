
class Advertisement:

    def __init__(self, url, title, date, location, delivery, condition, price, thumbnail):
        self.url = url
        self.title = title
        self.price = price
        self.date = date
        self.location = location
        self.delivery = delivery
        self.condition = condition
        self.thumbnail = thumbnail



class EmptyAdClass:

    def __init__(self):
        self.url = ""
        self.title = ""
        self.price = ""
        self.date = ""
        self.location = ""
        self.delivery = ""
        self.condition = ""
        self.thumbnail = ""
