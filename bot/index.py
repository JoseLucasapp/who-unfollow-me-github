from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bot.chrome_options import set_chrome_options


class App:
    def __init__(self, base_url):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(
            service=service, options=set_chrome_options())
        self.driver.get(base_url)
        self.action = webdriver.ActionChains(self.driver)
