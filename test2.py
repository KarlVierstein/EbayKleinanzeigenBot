import requests

url_login = "https://www.ebay-kleinanzeigen.de:443/m-einloggen.html"


headers = {
    'Host': 'www.ebay-kleinanzeigen.de',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0'
}

with requests.Session() as s:
    main_page_res = s.get('https://www.ebay-kleinanzeigen.de/', headers=headers)
    print(main_page_res.status_code)


    login_res = s.post(url_login, headers=headers)
    print(login_res.status_code)
    print(login_res.content)
