from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import re
import csv

SEARCH_QUERY = "Clothing, New York City, NY"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(options=chrome_options)

# Arrays to store scraped data
names, reviews, websites, info, links = [], [], [], [], []

# Function to save data to CSV with UTF-8 encoding
def save_to_csv():
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Review", "Info", "Website", "Links"])
        for row in zip(names, reviews, info, websites, links):
            writer.writerow(row)
    print("CSV file has been created.")

try:
    driver.get("https://www.google.com/maps")

    # Enter the search query and submit
    search_box = driver.find_element(By.XPATH, '//input[@id="searchboxinput"]')
    search_box.send_keys(SEARCH_QUERY, Keys.RETURN)
    time.sleep(15)

    index = 3
    while True:
        try:
            # Get the name of the place
            if "sponsored" in driver.find_element(By.CSS_SELECTOR,f"#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div:nth-child({index}) > div").get_attribute("innerText").lower():
                index+=2
                continue
            name_selector = (
                f"#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > "
                f"div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > "
                f"div:nth-child({index}) > div > div.bfdHYd.Ppzolf.OFBs3e > div.lI9IFe > div.y7PRA > div > div > "
                f"div.UaQhfb.fontBodyMedium > div.NrDZNb > div.qBF1Pd.fontHeadlineSmall"
            )
            name_element = driver.find_element(By.CSS_SELECTOR, name_selector)
            driver.execute_script("arguments[0].scrollIntoView();", name_element)
            names.append(name_element.text)

            # Get the review text
            review_selector = (
                f"#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > "
                f"div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > "
                f"div:nth-child({index}) > div > div.bfdHYd.Ppzolf.OFBs3e > div.lI9IFe > div.y7PRA > div > div > "
                f"div.UaQhfb.fontBodyMedium > div:nth-child(3) > div > span.e4rVHe.fontBodyMedium > span"
            )
            review_element = driver.find_element(By.CSS_SELECTOR, review_selector)
            reviews.append(review_element.get_attribute("aria-label"))

            # Open the details view by clicking on the link
            link_selector = (
                f"#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > "
                f"div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > "
                f"div:nth-child({index}) > div > a"
            )
            driver.find_element(By.CSS_SELECTOR, link_selector).click()
            time.sleep(0.1)

            # Wait for info section to load or retry after a short timeout
            start_time = time.time()
            while len(driver.find_elements(
                By.CSS_SELECTOR,
                '#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > '
                'div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde > div:nth-child(9)'
            )) == 0:
                if time.time() - start_time > 2:  # retry if timeout
                    driver.find_element(By.CSS_SELECTOR, link_selector).click()
                    time.sleep(0.1)
                    start_time = time.time()

            # Get info and clean up the text
            info_selector = (
                '#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > '
                'div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde > div:nth-child(9)'
            )
            info_element = driver.find_element(By.CSS_SELECTOR, info_selector)
            cleaned_text = re.sub(r'[^a-zA-Z0-9+\.\-\n]+','',info_element.get_attribute("innerText"))
            cleaned_text = re.sub(r'\n', ' ', cleaned_text)
            print(cleaned_text)
            info.append(cleaned_text)

            # Check if website link is available
            website = 0
            try:
                driver.find_element(
                    By.CSS_SELECTOR,
                    "#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > "
                    "div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde > div:nth-child(9) > div:nth-child(5) > a > div > "
                    "div.rogA2c.ITvuef > div.Io6YTe.fontBodyMedium.kR99db.fdkmkc"
                )
                website = 1
                link = driver.find_element(
                    By.CSS_SELECTOR,
                    "#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > "
                    "div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde > div:nth-child(9) > div:nth-child(5) > a > div > "
                    "div.rogA2c.ITvuef > div.Io6YTe.fontBodyMedium.kR99db.fdkmkc"
                ).text
                links.append(link)
            except:
                links.append("")
                pass
            websites.append(website)
            time.sleep(0.1)

            # Close details view and increment index
            driver.find_element(
                By.CSS_SELECTOR,
                "#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > "
                "div.BHymgf.eiJcBe.bJUD0c > div > div > div:nth-child(3) > span > button > span > svg"
            ).click()
            time.sleep(1)
            index += 2
        except Exception as e:
            print(f"Error on index {index}: {e}")
            save_to_csv()
            break
finally:
    driver.quit()
