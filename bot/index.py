from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


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

    def print_color(self, text):
        RESET = '\033[0m'

        print(f'\033[31m {text}{RESET}')

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

        if len(not_following_you) > 0:
            print(f'\033[0m\nNOT FOLLOWING YOU:\n')
            for follower in not_following_you:
                self.print_color(follower)
        else:
            print(f'\033[92mGreat! Everyone is following you.')

        if len(not_followed_by_you) > 0:
            print(f'\033[0m\nYOU ARE NOT FOLLOWING:\n')
            for following in not_followed_by_you:
                self.print_color(following)
        else:
            print(f'\033[92mAwesome! You are following everyone back.')

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
                    # Captura os seguidores na página atual
                    self.get_type(type)

                    # Verifica se há um botão de paginação
                    next_btn = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//*[@class="pagination"]/*[2]')
                        )
                    )

                    if next_btn and next_btn.tag_name == 'a' and next_btn.get_attribute('rel') == 'nofollow' and next_btn.text == 'Next':
                        self.wait_for_page_load()
                        sleep(1)
                        next_btn.click()
                    else:
                        print(f"No more pages to load for {type}.")
                        break
                except TimeoutException:
                    print(f"No pagination button found for {type}.")
                    break
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
                    continue
        finally:
            stop_event.set()
            running_thread.join()
