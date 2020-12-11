from bs4 import BeautifulSoup


class NewsParser:

    def __init__(self, driver):
        self.driver = driver


    def parse(self, url):
        self.driver.get(url)
        html = self.driver.page_source
        soup = BeautifulSoup(html, features = 'lxml')
        news_title = soup.find('div', {'class': 'news-header__title'}).text
        print(f"selenium news title: {news_title.strip()}")
        self.driver.delete_all_cookies()
        return ''
