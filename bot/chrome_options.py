from selenium.webdriver.chrome.options import Options


def set_chrome_options() -> Options:
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("start-maximized")
    # chrome_options.add_argument("--auto-open-devtools-for-tabs")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option("detach", True)
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options
