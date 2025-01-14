import csv
import re
from selenium.common.exceptions import NoSuchElementException

def save_to_csv(names, reviews, info, websites, links, file_name='output.csv'):
    """
    Save the scraped data to a CSV file.
    """
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Review", "Info", "Website", "Links"])
        for row in zip(names, reviews, info, websites, links):
            writer.writerow(row)
    print(f"CSV file '{file_name}' has been created.")

def get_element_text(driver, selector, attribute="innerText"):
    """
    Retrieve text or an attribute from an element, handling exceptions.
    """
    try:
        element = driver.find_element_by_css_selector(selector)
        if attribute == "innerText":
            return element.text
        return element.get_attribute(attribute)
    except NoSuchElementException:
        return ""

def clean_text(text):
    """
    Clean text by removing special characters and unnecessary whitespace.
    """
    cleaned_text = re.sub(r'[^a-zA-Z0-9+\.\-\n]+', '', text)
    return re.sub(r'\n', ' ', cleaned_text)
