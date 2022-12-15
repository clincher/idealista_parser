# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests

from bs4 import BeautifulSoup


def parse():
    page = 1
    s = requests.session()
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/87.0.4280.141 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                  'image/avif,image/webp,image/apng,*/*;q=0.8,application/'
                  'signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru,fil;q=0.9,pt;q=0.8,pt-BR;q=0.7,pt-PT;q=0.6,es;q=0.5,en;q=0.4',
        'cache-control': 'no-cache',
        'cookie': 'afUserId=6daf1859-1f83-43c5-b67c-1dbcae427392-p',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'upgrade-insecure-requests': '1'
    }
    s.headers.update(headers)
    response = s.get(
        'https://www.idealista.com/en/venta-viviendas/almeria-provincia/')
    html = response.content.decode('utf-8')

    while True:
        if page == 1:
            url = 'https://www.idealista.com/en/venta-viviendas/' \
                  'almeria-provincia/'
        else:
            url = 'https://www.idealista.com/en/venta-viviendas/' \
                  'almeria-provincia/pagina-{}.htm'.format(page)
        response = requests.get(url)
        html = response.content.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse()
