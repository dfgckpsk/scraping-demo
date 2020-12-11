import requests


class Driver:

    def get(self, **kwargs):
        return Webdriver()


class Webdriver:

    def get(self, url):
        response = requests.get('http://localhost:8050/render.html',
                     params={'url': url,
                             'wait': 2})
        return response


    def close(self):
        pass
