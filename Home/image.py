from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def scraped_news(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=chrome_options)

        driver.get(url)
        wait = WebDriverWait(driver, 10)

        for _ in range(5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.uwU81')))

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            image_urls = extract_image_urls(soup)

            for image_url in image_urls:
                yield image_url

            time.sleep(2)

    finally:
        driver.quit()

def extract_image_urls(soup):
    articles = soup.find_all('div', class_='uwU81')

    for article in articles:
        image = article.find('img')

        if image:
            for attr in ['src', 'data-src']:
                if attr in image.attrs and image[attr].endswith(('.jpg', '.jpeg', '.png')):
                    image_url = image[attr]
                    yield image_url

# Example usage:
if __name__ == "__main__":
    url_to_scrape = "https://timesofindia.indiatimes.com/topic/yelahanka"

    # Access image URLs one by one
    for url in scraped_news(url_to_scrape):
        print(f"Processing image URL: {url}")

        # Add your code here to use the image URL as needed
