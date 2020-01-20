import itertools

import requests
from bs4 import BeautifulSoup


def crawler():
    BASE_URL = "https://news.ycombinator.com/news"

    for page in itertools.count(1):
        response = requests.get(BASE_URL, params={'p': page})
        document = BeautifulSoup(response.text, 'html.parser')
        for link_wrap in document.select('.athing'):
            link = link_wrap.select_one('.storylink')
            rank = link_wrap.select_one('.rank')

            print('id :', link_wrap.get('id'))
            print('rank :', rank.text.strip('.'))
            print('link :', link.get('href'))
            print('text :', link.text)
            print()


if __name__ == '__main__':
    crawler()


