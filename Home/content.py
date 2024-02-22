import requests
from bs4 import BeautifulSoup
import re

def remove_unknown_characters(input_text):
    allowed_chars_pattern = re.compile('[a-zA-Z0-9, ]')
    filtered_text = ''.join(allowed_chars_pattern.findall(input_text))
    return filtered_text

def scrape_locations(url):
    locations_list = []

    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract location from each article
        articles = soup.find_all('div', class_='uwU81')  # Adjust the class based on the website's structure

        for article in articles:
            location = article.find('p', class_='oxXSK o58kM')
            location_text = location.text.strip() if location else "N/A"
            filtered_location = remove_unknown_characters(location_text)
            locations_list.append(filtered_location)

    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage. Error: {e}")

    return locations_list

# Example usage:
if __name__ == "__main__":
    url_to_scrape = "https://timesofindia.indiatimes.com/topic/yelahanka"
    locations = scrape_locations(url_to_scrape)

    for index, location in enumerate(locations, start=1):
        print(f"Article {index}  {location}")
