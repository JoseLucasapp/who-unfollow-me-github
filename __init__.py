from bot.index import App

if __name__ == '__main__':
    user = 'joselucasapp'
    base_url = f'https://github.com/{user}'
    bot = App(base_url=base_url)
    bot.next_button('followers')
    bot.next_button('followings')
    bot.find()
