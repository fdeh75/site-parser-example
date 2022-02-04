from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-mazda/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
HOST = 'https://auto.ria.com'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # items = soup.find_all('section', class_='proposition  ')
    items = soup.select('#searchResult > div > section')

    cars = []
    for item in items:
        cars.append({
            'name': item.select_one('.proposition_name').get_text(strip=True),
            # 'title': item.find('span', class_='link').get(section),
            # 'link': HOST + item.find('a', class_='proposition_link').get(href),
        })
    pprint(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
