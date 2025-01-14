# constants.py

from selenium.webdriver.chrome.options import Options

SEARCH_QUERY = "Clothing, New York City, NY"

# Chrome options setup
def get_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")
    return chrome_options
