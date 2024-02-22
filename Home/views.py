from django.shortcuts import render
from django.conf import settings
from Home.models import Report
from Home.image import scrape_image_urls
from Home.headings import scrape_news
from Home.content import scrape_locations
import random
# from .models import Report

def Yelahanka(request):
    return render(request, 'Yelahanka.html')

def Anekal(request):
    
    url_to_scrape = "https://timesofindia.indiatimes.com/topic/anekal"

    # Assuming scrape_news returns a list of scraped headings
    scraped_headings = scrape_news(url_to_scrape)

    # Assuming scrape_locations returns a list of scraped locations
    scraped_locations = scrape_locations(url_to_scrape)

    # Assuming scraped_image_urls returns a list of image URLs
    image_urls = scrape_image_urls(url_to_scrape)

    # Ensure each heading has an image URL or use a placeholder
    zipped_data = []

    # Replace missing image URLs with a randomly chosen placeholder image URL
    num_placeholders = 6  # Adjust the number of placeholders as needed
    placeholder_image_urls = [
        'https://cdn.pixabay.com/photo/2016/02/01/00/56/news-1172463_640.jpg',
        'https://thumbs.dreamstime.com/b/news-woodn-dice-depicting-letters-bundle-small-newspapers-leaning-left-dice-34802664.jpg',
        'https://cdn.create.vista.com/api/media/small/5394402/stock-photo-newspapers',
        'https://images.freeimages.com/images/large-previews/daf/newspaper-1516622.jpg?fmt=webp&w=500',
        'https://thumbs.dreamstime.com/b/local-news-25068677.jpg','https://www.shutterstock.com/image-photo/man-reading-newspaper-headline-local-260nw-594183902.jpg',''
    ]

    default_placeholder_images = [
        random.choice(placeholder_image_urls) for _ in range(num_placeholders)
    ]

    for i in range(len(scraped_headings)):
        location = scraped_locations[i] if i < len(scraped_locations) else "N/A"
        image_url = image_urls[i] if i < len(image_urls) else default_placeholder_images[i % num_placeholders]
        zipped_data.append((scraped_headings[i], location, image_url))

    return render(request, 'Anekal.html', {'zipped_data': zipped_data})



# Create your views here.
def home(request):
    return render(request,'index.html')

def data(request):
    items = Report.objects.all()
    return render(request, 'database.html',{'data' : items})

def CitizenReport(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        description = request.POST['description']

        instance = Report(name = name, email = email, phone = phone, subject = subject, description = description)
        instance.save()
        print()
        print()
        print(name,email,phone,subject,description)
        print()
        print()

    return render(request,'CitizenReport.html')
def Banashankari(request):
    return render(request,'Banashankari.html')

#def Yelahanka(request):
    path = str(settings.BASE_DIR)+str('/format/modified.txt')
    try:
        with open(path,'r')as file:
            contents = file.read()
    except FileNotFoundError:
        contents = "NEWS NOT FOUND (exception)."
    return render(request, 'Yelahanka.html',{'file_contents':contents})

    # #return HttpResponse("HELLO--home")
    # '''scrape = {} Pass your scraped content here and make it appear in the webpage!
    # remember render takes three arguemenets!
    # test-1 below
    # '''
    # path = str(settings.BASE_DIR)+str('/Textfiles/buffer.txt')
    # try:
    #     with open(path,'r')as file:
    #         contents = file.read()
    # except FileNotFoundError:
    #     contents = "File Not Found."
    # return render(request, 'locations.html',{'file_contents':contents})
