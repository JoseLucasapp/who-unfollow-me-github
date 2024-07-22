from bot.index import App

if __name__ == '__main__':
    github_username = input(
        "Please enter your GitHub username (without the '@'): ")
    base_url = f'https://github.com/{github_username}'
    bot = App(base_url=base_url)
    bot.next_button('followers')
    bot.next_button('followings')
    bot.find()
