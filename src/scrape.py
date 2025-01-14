from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from constants import SEARCH_QUERY, CHROME_OPTIONS
from helpers import save_to_csv, get_element_text, clean_text

# Initialize the driver with Chrome options
driver = webdriver.Chrome(options=CHROME_OPTIONS)

# Arrays to store scraped data
names, reviews, websites, info, links = [], [], [], [], []

try:
    # Navigate to Google Maps
    driver.get("https://www.google.com/maps")

    # Enter the search query and submit
    search_box = driver.find_element(By.XPATH, '//input[@id="searchboxinput"]')
    search_box.send_keys(SEARCH_QUERY, Keys.RETURN)
    time.sleep(15)

    index = 3
    while True:
        try:
            # Check for sponsored content and skip if found
            sponsored_selector = (
                f"#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > "
                f"div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > "
                f"div:nth-child({index}) > div"
            )
            if "sponsored" in get_element_text(driver, sponsored_selector).lower():
                index += 2
                continue

            # Scrape name
            name_selector = (
                f"#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > "
                f"div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > "
                f"div:nth-child({index}) > div > div.bfdHYd.Ppzolf.OFBs3e > div.lI9IFe > div.y7PRA > div > div > "
                f"div.UaQhfb.fontBodyMedium > div.NrDZNb > div.qBF1Pd.fontHeadlineSmall"
            )
            name = get_element_text(driver, name_selector)
            names.append(name)

            # Scrape review
            review_selector = (
                f"#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > "
                f"div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > "
                f"div:nth-child({index}) > div > div.bfdHYd.Ppzolf.OFBs3e > div.lI9IFe > div.y7PRA > div > div > "
                f"div.UaQhfb.fontBodyMedium > div:nth-child(3) > div > span.e4rVHe.fontBodyMedium > span"
            )
            review = get_element_text(driver, review_selector, attribute="aria-label")
            reviews.append(review)

            # Scrape additional details
            link_selector = (
                f"#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > "
                f"div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd > "
                f"div:nth-child({index}) > div > a"
            )
            driver.find_element(By.CSS_SELECTOR, link_selector).click()
            time.sleep(0.1)

            info_selector = (
                '#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > '
                'div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde > div:nth-child(9)'
            )
            info_text = get_element_text(driver, info_selector)
            cleaned_info = clean_text(info_text)
            info.append(cleaned_info)

            # Scrape website link if available
            website_selector = (
                "#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > "
                "div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde > div:nth-child(9) > div:nth-child(5) > a"
            )
            website_link = get_element_text(driver, website_selector, attribute="href")
            websites.append(1 if website_link else 0)
            links.append(website_link or "")

            # Close details view and move to the next item
            driver.find_element(
                By.CSS_SELECTOR,
                "#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > "
                "div.BHymgf.eiJcBe.bJUD0c > div > div > div:nth-child(3) > span > button > span > svg"
            ).click()
            time.sleep(1)
            index += 2

        except Exception as e:
            print(f"Error on index {index}: {e}")
            save_to_csv(names, reviews, info, websites, links)
            break

finally:
    driver.quit()
