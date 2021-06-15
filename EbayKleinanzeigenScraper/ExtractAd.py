from lxml import html
from utils.date import get_date, get_date_tmrw
from advertisement import Advertisement

def exctract_from_ad(element_parser, listener=False):
    title = element_parser.xpath('div[2]/div[2]/h2/a/text()')[0]
    selling_location = element_parser.xpath('div[2]/div[1]/div[1]/text()')
    selling_date = str(element_parser.xpath('div[2]/div[1]/div[2]/text()')[1].strip())
    if selling_date[0:5] == "Heute":
        selling_date = selling_date[:0] + get_date() + selling_date[5:]
    elif selling_date[0:7] == "Gestern":
        selling_date = selling_date[:0] + get_date_tmrw() + selling_date[7:]
    url = "https://ebay-kleinanzeigen.de" + element_parser.xpath('@data-href')[0]
    try:
        thumbnail = element_parser.xpath('div[1]/a/div/@data-imgsrc')[0]

    except IndexError:
        thumbnail = "https://www.happypostcards.de/img/p/de-default-big_default.jpg"

    price = element_parser.xpath('div[2]/div[2]/p[2]/text()')[0].strip()

    return Advertisement(url=url, title=title, date=selling_date, location=selling_location, delivery=None,
                                   condition=None, price=price, thumbnail=thumbnail[0])