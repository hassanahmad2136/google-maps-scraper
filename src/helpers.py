import csv
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def save_to_csv(names, reviews, info, websites, links, file_name='../output/output.csv'):
    """
    Save the scraped data to a CSV file.
    """
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Review", "Info", "Website", "Links"])
        for row in zip(names, reviews, info, websites, links):
            writer.writerow(row)
    print(f"CSV file '{file_name}' has been created.")
