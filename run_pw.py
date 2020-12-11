from pw.AsyncParserHandler import AsyncParserHandler
from pw.NewsParser import NewsParser


if __name__ == '__main__':

    config = {'request_number': 1,
              'browser': 'chrome',
              'headless': True,
              'random_delay': (1, 3)}

    links = ['https://people.onliner.by/2020/10/15/samolet-lukashenko-prizemlilsya-v-gamburge-na-obsluzhivanie-no-profsoyuz-lufthansa-technik-vystupil-s-zayavleniem',
             'https://people.onliner.by/2020/10/15/xronika-dnya-tixanovskaya-obratilas-k-studentam-i-prepodavatelyam']

    handler = AsyncParserHandler(NewsParser, config)
    result = handler.parse_links(links)