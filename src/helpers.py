from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

def setup_driver():
    """Sets up the Selenium WebDriver with Chrome options."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=chrome_options)

def save_to_csv(names, reviews, info, websites, links):
    """Saves the scraped data to a CSV file."""
    with open('output/output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Review", "Info", "Website", "Links"])
        for row in zip(names, reviews, info, websites, links):
            writer.writerow(row)
    print("CSV file has been created.")
