from django.shortcuts import render
from django.conf import settings
from Home.models import Report
from Home.image import scraped_news
from Home.test1 import scrape_news
from Home.content import scrape_locations
from django.shortcuts import render
from django.conf import settings
# from .models import Report

def Yelahanka(request):
    url_to_scrape = "https://timesofindia.indiatimes.com/topic/yelahanka"
    # Assuming scrape_news returns a list of scraped headings
    scraped_headings = scrape_news(url_to_scrape)
    # Assuming scrape_locations returns a list of scraped locations
    scraped_locations = scrape_locations(url_to_scrape)
    # Assuming scraped_image_urls returns a list of image URLs
    image_urls = scraped_news(url_to_scrape)
    path = str(settings.BASE_DIR) + '/format/modified.txt'
    try:
        with open(path, 'r') as file:
            contents = file.read()
    except FileNotFoundError:
        contents = "NEWS NOT FOUND (exception)."

    # Zip headings, locations, and image URLs in the view
    zipped_data = list(zip(scraped_headings, scraped_locations, image_urls))

    return render(request, 'Yelahanka.html', {'file_head': contents, 'zipped_data': zipped_data})

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

def Anekal(request):
    return render(request,'Anekal.html')

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
