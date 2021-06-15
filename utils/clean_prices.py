def filter_prices(given_list):
    prices = list()
    for element in given_list:
        price_elements = element.price.split(" ")
        if len(price_elements) != 0:
            for price_element in price_elements:
                if price_element == "€" or price_element == "" or price_element == " " or "VB" in price_element or 'VB' in price_element:
                    price_elements.remove(price_element)
            try:
                if "." in price_elements[0]:
                    price_elements[0] = price_elements[0].replace(".", "")
                prices.append(int(price_elements[0]))
            except IndexError:
                continue

    return prices