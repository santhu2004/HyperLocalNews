import requests
import re
from bs4 import BeautifulSoup
import sys
import os

def remove_unknown_characters(input_text):
    allowed_chars_pattern = re.compile('[a-zA-Z0-9, ]')
    filtered_text = ''.join(allowed_chars_pattern.findall(input_text))
    return filtered_text

def scrape_news(url):
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and write headings, locations, contents, and image URLs to output.txt
        articles = soup.find_all('div', class_='uwU81')  # Adjust the class based on the website's structure

        output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output.txt')

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            sys.stdout = output_file  # Redirect standard output to the file

            for article in articles:
                heading = article.find('div', class_='fHv_i o58kM')
                location = article.find('p', class_='oxXSK o58kM')
                content = article.find('div', class_='ZxBIG')
                image = article.find('img')  # Adjust the class accordingly

                heading_text = heading.text.strip() if heading else "N/A"
                location_text = location.text.strip() if location else "N/A"
                content_text = content.text.strip() if content else "N/A"

                # Check both 'src' and 'data-src' attributes for the image URL
                image_url = ""
                if image:
                    for attr in ['src', 'data-src']:
                        if attr in image.attrs and image[attr].endswith(('.jpg', '.jpeg', '.png')):
                            image_url = image[attr]
                            break

                # Example usage:
                filtered_head = remove_unknown_characters(heading_text)
                filtered_loc = remove_unknown_characters(location_text)
                filtered_con = remove_unknown_characters(content_text)

                print(f"Heading: {filtered_head}\nContent: {filtered_loc}\n")

    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage. Error: {e}")

# Example usage:
if __name__ == "__main__":
    url_to_scrape = "https://timesofindia.indiatimes.com/topic/yelahanka"
    scrape_news(url_to_scrape)
