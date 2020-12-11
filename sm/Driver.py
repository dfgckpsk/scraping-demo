from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options, FirefoxBinary


class Driver:

    def __init__(self, browser_path):
        self.browser_path = browser_path


    def get_firefox(self, proxy, useragent):

        profile = webdriver.FirefoxProfile()
        if useragent is not None:
            profile.set_preference("general.useragent.override", useragent)
        firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True

        options_sel = {

            'connection_timeout': 5,
            'suppress_connection_errors': True
        }

        if proxy is not None:
            options_sel['proxy'] = {
                'http': proxy.get_init_string(),
                'https': proxy.get_init_string().replace('http', 'https')
            }
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--user-agent={}'.format(useragent))
        binary = FirefoxBinary(self.browser_path)
        driver_ = webdriver.Firefox(capabilities=firefox_capabilities,
                                    options=options,
                                    firefox_binary = binary,
                                    firefox_profile = profile,
                                    timeout = 5,
                                    seleniumwire_options = options_sel)
        HEADERS = {}
        HEADERS['User-Agent'] = useragent
        driver_.header_overrides = HEADERS

        return driver_


    def get(self, proxy=None, useragent=None):

        """
        :param proxy: 192.168.0.104:5444
        :return:
        """

        return self.get_firefox(proxy, useragent)
