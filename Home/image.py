import requests
from bs4 import BeautifulSoup
import random

def scrape_image_urls(url):
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and store image URLs in a list
        articles = soup.find_all('div', class_='uwU81')  # Adjust the class based on the website's structure

        image_urls = []
        for article in articles:
            image = article.find('img')  # Adjust the class accordingly

            # Check both 'src' and 'data-src' attributes for the image URL
            if image:
                for attr in ['src', 'data-src']:
                    if attr in image.attrs and image[attr].endswith(('.jpg', '.jpeg', '.png')):
                        if image[attr] == "https://static.toiimg.com/thumb/imgsize-123456,msid-78553754,width-300,resizemode-4/78553754.jpg":
                            # Replace with a random placeholder image URL
                            placeholder_images = [ 'https://cdn.pixabay.com/photo/2016/02/01/00/56/news-1172463_640.jpg',
        'https://thumbs.dreamstime.com/b/news-woodn-dice-depicting-letters-bundle-small-newspapers-leaning-left-dice-34802664.jpg',
        'https://cdn.create.vista.com/api/media/small/5394402/stock-photo-newspapers',
        'https://images.freeimages.com/images/large-previews/daf/newspaper-1516622.jpg?fmt=webp&w=500',
        'https://thumbs.dreamstime.com/b/local-news-25068677.jpg','https://www.shutterstock.com/image-photo/man-reading-newspaper-headline-local-260nw-594183902.jpg'
                                
                            ]
                            image_urls.append(random.choice(placeholder_images))
                        else:
                            image_urls.append(image[attr])
                        break

        return image_urls

    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage. Error: {e}")
        return None

# Example usage:
if __name__ == "_main_":
    url_to_scrape = "https://timesofindia.indiatimes.com/topic/yelahanka"
    image_urls = scrape_image_urls(url_to_scrape)

    if image_urls:
        for url in image_urls:
            print(f"Image URL: {url}")