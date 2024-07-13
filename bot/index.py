from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from bot.chrome_options import set_chrome_options


class App:
    def __init__(self, base_url):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(
            service=service, options=set_chrome_options())
        self.action = webdriver.ActionChains(self.driver)
        self.tab_followers = '?tab=followers'
        self.tab_following = '?tab=following'
        self.driver.get(f'{base_url}{self.tab_followers}')

    def get_followers(self):
        followers = self.driver.find_elements(
            By.XPATH, '//*[@id="user-profile-frame"]/div/div/div[2]/a/span[2]')

    def next_button(self):
        next_btn = self.driver.find_element(
            By.XPATH, '//*[@class="pagination"]/*[2]').text
