import requests
from bs4 import BeautifulSoup
import re

def remove_unknown_characters(input_text):
    allowed_chars_pattern = re.compile('[a-zA-Z0-9, ]')
    filtered_text = ''.join(allowed_chars_pattern.findall(input_text))
    return filtered_text

def scrape_news(url):
    headings = []
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and write headings to the list
        articles = soup.find_all('div', class_='uwU81')  # Adjust the class based on the website's structure

        for article in articles:
            heading = article.find('div', class_='fHv_i o58kM')

            heading_text = heading.text.strip() if heading else "N/A"

            # Example usage:
            filtered_head = remove_unknown_characters(heading_text)
            headings.append(filtered_head)

    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage {url}. Error: {e}")

    return headings

# Example usage:
if __name__ == "__main__":
    url_to_scrape = "https://timesofindia.indiatimes.com/topic/"
    scraped_headings = scrape_news(url_to_scrape)

    # Display the number of headings
    num_headings = len(scraped_headings)
    print(f"Number of Headings: {num_headings}")

    # Display each heading
    for i, heading in enumerate(scraped_headings, start=1):
        print(f"{i}. {heading}")
