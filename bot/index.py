from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from bot.chrome_options import set_chrome_options


class App:
    def __init__(self, base_url):
        self.base_url = base_url
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(
            service=service, options=set_chrome_options())
        self.action = webdriver.ActionChains(self.driver)
        self.tab_followers = '?tab=followers'
        self.tab_following = '?tab=following'
        self.followers = []
        self.followings = []

    def get_followers_and_followers(self, array):
        follow = self.driver.find_elements(
            By.XPATH, '//*[@id="user-profile-frame"]/div/div/div[2]/a/span[2]')

        for i in follow:
            array.append(i.text)

    def get_type(self, type):
        if type == 'followers':
            self.get_followers_and_followers(self.followers)
        else:
            self.get_followers_and_followers(self.followings)

    def find(self):
        print('You are not following:\n')
        for follower in self.followers:
            if not follower in self.followings:
                print(follower)

        print('Not follow you:\n')
        for following in self.followings:
            if following not in self.followers:
                print(following)

    def next_button(self, type):
        if type == 'followers':
            self.driver.get(f'{self.base_url}{self.tab_followers}')
        else:
            self.driver.get(f'{self.base_url}{self.tab_following}')

        while True:
            try:
                next_btn = self.driver.find_element(
                    By.XPATH, '//*[@class="pagination"]/*[2]')

                if next_btn.tag_name == 'a' and next_btn.get_attribute('rel') == 'nofollow' and next_btn.text == 'Next':
                    self.get_type(type)
                    next_btn.click()
                else:
                    break
            except:
                continue
