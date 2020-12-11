from bs4 import BeautifulSoup


class NewsParser:

    def __init__(self, driver):
        self.driver = driver


    def parse(self, url):
        response = self.driver.get(url)
        html = response.content
        soup = BeautifulSoup(html, features = 'lxml')
        news_title = soup.find('div', {'class': 'news-header__title'}).text
        print(f"splash news title: {news_title}")
        return news_title
