from bs4 import BeautifulSoup


class NewsParser:

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config


    async def _parse(self, url, **kwargs):
        await self.driver.goto(url, timeout = 0)
        html = await self.driver.content()
        soup = BeautifulSoup(html, features = 'lxml')
        news_title = soup.find('div', {'class': 'news-header__title'}).text
        print(f"playwright news title: {news_title.strip()}")
        return True


    async def parse(self, url, **kwargs):
        try:
            result = await self._parse(url, **kwargs)
            return result
        except BaseException as e:
            print('exception', e)
            return None
