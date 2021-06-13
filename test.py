import requests

session = requests.session()

main_page_url = "https://www.ebay-kleinanzeigen.de:443/"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "de,en-US;q=0.7,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Upgrade-Insecure-Requests": "1", "Te": "trailers", "Connection": "close"}
main_page_res = session.get(main_page_url, headers=burp0_headers)


burp0_url = "https://api.ebay-kleinanzeigen.de:443/consent-v2/defaultString"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0", "Accept": "*/*", "Accept-Language": "de,en-US;q=0.7,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Access-Control-Request-Method": "GET", "Access-Control-Request-Headers": "application", "Referer": "https://www.ebay-kleinanzeigen.de/", "Origin": "https://www.ebay-kleinanzeigen.de", "Te": "trailers", "Connection": "close"}
res = session.options(burp0_url, headers=burp0_headers)

