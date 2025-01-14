from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from helpers import save_to_csv, setup_driver
from constants import SEARCH_QUERY
import time
import re

# Initialize driver
driver = setup_driver()

# Arrays to store scraped data
names, reviews, websites, info, links = [], [], [], [], []

try:
    driver.get("https://www.google.com/maps")
    search_box = driver.find_element(By.XPATH, '//input[@id="searchboxinput"]')
    search_box.send_keys(SEARCH_QUERY, Keys.RETURN)
    time.sleep(15)

    index = 3
    while True:
        try:
            # Fetch data (modularize scraping logic if needed)
            # Example: fetch_name(driver, index)
            name_element = driver.find_element(By.CSS_SELECTOR, "CSS_SELECTOR_FOR_NAME")
            names.append(name_element.text)
            # Similar for other data...
            index += 2
        except Exception as e:
            print(f"Error on index {index}: {e}")
            save_to_csv(names, reviews, info, websites, links)
            break
finally:
    driver.quit()

