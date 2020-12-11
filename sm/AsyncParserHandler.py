import asyncio
from concurrent.futures.thread import ThreadPoolExecutor
from fake_useragent import UserAgent
from .Driver import Driver

import random
import time


class AsyncParserHandler:

    def __init__(self, parser_class, config, driver):

        self.parser_class = parser_class
        self.driver = driver
        self.config = config
        self.min_delay, self.max_delay = self.config.get('random_delay', (0, 2.0))

        request_number = config.get('request_number')
        self.request_number = request_number if request_number is not None else self.drivers
        self.executor = ThreadPoolExecutor(self.request_number)


    def parse_link(self, link, driver):

        useragent = UserAgent().random
        try:

            time.sleep(random.uniform(self.min_delay, self.max_delay))
            webdriver = driver.get(proxy = None,
                                   useragent=useragent)
            parser = self.parser_class(webdriver).parse(link)
            webdriver.close()
            if parser is not None:
                print('Success')
            else:
                print('Probably captcha')
            return parser

        except:
            print('excpet', link)


    def parse_links(self, links):

        tasks = []
        self.loop = asyncio.get_event_loop()

        for link in links:
            task = self.loop.run_in_executor(self.executor, self.parse_link, link, self.driver)
            tasks.append(task)

        results = self.loop.run_until_complete(asyncio.gather(*tasks))
        self.loop.close()
        return results
