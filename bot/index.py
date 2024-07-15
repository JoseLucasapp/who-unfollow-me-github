from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import threading
import asyncio

from bot.chrome_options import set_chrome_options
from system_settings import System_settings

from time import sleep


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
        self.NAVY_BLUE = '\033[38;5;17m'
        self.RED = '\033[31m'

    def print_color(self, text, color):
        RESET = '\033[0m'

        print(f'{color}{text}{RESET}')

    def wait_for_page_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(lambda driver: driver.execute_script(
            'return document.readyState') == 'complete')

    def get_followers_and_followers(self, array):
        follow = self.driver.find_elements(
            By.XPATH, '//*[@id="user-profile-frame"]/div/div/div[2]/a/span[2]')

        for i in follow:
            if i.text not in array:
                array.append(i.text)

    def get_type(self, type):
        if type == 'followers':
            self.get_followers_and_followers(self.followers)
        else:
            self.get_followers_and_followers(self.followings)

    def find(self):

        not_following_you = [
            follower for follower in self.followings if follower not in self.followers]
        not_followed_by_you = [
            following for following in self.followers if following not in self.followings]

        print('\nNOT FOLLOWING YOU:\n')
        for follower in not_following_you:
            self.print_color(follower, self.RED)

        print('\nYOU ARE NOT FOLLOWING:\n')
        for following in not_followed_by_you:
            self.print_color(following, self.NAVY_BLUE)

    def running(self, stop_event):
        dots = '.'
        count = 1
        while not stop_event.is_set():
            sleep(1)
            System_settings.check_os()
            print(f'Searching{dots}')

            if count == 3:
                dots = ''
                count = 0

            count += 1
            dots = '.' * count
        System_settings.check_os()

    def next_button(self, type):

        stop_event = threading.Event()

        running_thread = threading.Thread(
            target=self.running, args=(stop_event,))
        running_thread.start()

        try:
            if type == 'followers':
                self.driver.get(f'{self.base_url}{self.tab_followers}')
            else:
                self.driver.get(f'{self.base_url}{self.tab_following}')

            while True:
                try:
                    next_btn = WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//*[@class="pagination"]/*[2]'))
                    )

                    if next_btn.tag_name == 'a' and next_btn.get_attribute('rel') == 'nofollow' and next_btn.text == 'Next':
                        self.wait_for_page_load()
                        sleep(1)
                        self.get_type(type)
                        next_btn.click()
                    else:
                        break
                except:
                    continue
        finally:
            stop_event.set()
            running_thread.join()
