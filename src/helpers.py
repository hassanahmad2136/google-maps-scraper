# helpers.py

import csv

def save_to_csv(names, reviews, info, websites, links, filename="output.csv"):
    """
    Save scraped data to a CSV file.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Review", "Info", "Website", "Links"])
        for row in zip(names, reviews, info, websites, links):
            writer.writerow(row)
    print("CSV file has been created.")
