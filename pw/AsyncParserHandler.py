import asyncio
import random

from fake_useragent import UserAgent
from playwright import async_playwright


class AsyncParserHandler:

    def __init__(self, parser_class, config):

        self.parser_class = parser_class
        self.config = config
        self.min_delay, self.max_delay = self.config.get('random_delay', (0, 2.0))

        request_number = config.get('request_number')
        self.request_number = request_number if request_number is not None else self.drivers
        self.pages_per_browser = self.config.get('pages_per_browser', 1)
        self.fail_count_to_interrupt = self.config.get('fail_count_to_interrupt', 5)


    def browser_by_type(self, p):
        browser_type = p.webkit

        if self.config['browser'] == 'chrome':
            browser_type = p.chromium
        elif self.config['browser'] == 'firefox':
            browser_type = p.firefox
        return browser_type


    async def parse_links_task(self, link):

        async with async_playwright() as p:
            browser_type = self.browser_by_type(p)

            useragent = UserAgent().random

            browser = await browser_type.launch(headless = self.config.get('headless', True))
            page = await browser.newPage(userAgent = useragent, viewport = {"width": 1600, "height": 900})

            delay = random.uniform(self.min_delay, self.max_delay)
            await asyncio.sleep(delay)

            try:
                parser_obj = self.parser_class(page,
                                               config=self.config)
                parser = await parser_obj.parse(link)

                if parser is not None:
                    print('Success')
                else:
                    print('Probably captcha')
                return parser


            except BaseException as e:
                print('except', link, e)
                print('Fail')

            await browser.close()


    async def parse_links_async(self, links):

        tasks = []
        for link in links:
            tasks.append(self.parse_links_task(link))

        results = await asyncio.gather(*tasks)
        return results


    def parse_links(self, links):

        return asyncio.run(self.parse_links_async(links))
