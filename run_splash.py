from sm.AsyncParserHandler import AsyncParserHandler
from splash.NewsParser import NewsParser
from splash.Driver import Driver


if __name__ == '__main__':

    config = {'request_number': 1,
              'random_delay': (1, 3)}

    links = ['https://people.onliner.by/2020/10/15/samolet-lukashenko-prizemlilsya-v-gamburge-na-obsluzhivanie-no-profsoyuz-lufthansa-technik-vystupil-s-zayavleniem',
             'https://people.onliner.by/2020/10/15/xronika-dnya-tixanovskaya-obratilas-k-studentam-i-prepodavatelyam']

    driver = Driver()
    handler = AsyncParserHandler(NewsParser, config, driver)
    result = handler.parse_links(links)