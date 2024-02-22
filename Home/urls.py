from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('CitizenReport', views.CitizenReport, name="Citizen"),
    path('CitizenInput',views.CitizenInput, name = 'CitizenInput'),
    path('Contact_Us',views.Contact_Us, name = 'Contact_Us'),

    path('Anekal',views.Anekal, name = 'Anekal'),
    path('Banashankari',views.Banashankari, name = 'Banashankari'),
    path('Banneraghatta',views.Banneraghatta, name = 'Bannerghatta'),
    path('Bellandur_Lake',views.Bellandur_Lake, name = 'Bellanduru'),
    path('Bommanahalli',views.Bommanahalli, name = 'Bommanahalli'),
    path('Cubbon_Park',views.Cubbon_Park, name = 'Cubbon_Park'),
    path('Kengeri',views.Kengeri, name = 'Kengeri'),
    path('Kormangla',views.Kormangla, name = 'Kormangala'),
    path('Nagasandra',views.Nagasandra, name = 'Nagasandara'),
    path('Yelahanka',views.Yelahanka, name = 'Yelahanka'),
  
    # path('', views.about, name="about"),
    # path('contact', views.contact, name="contact"),
    # path('Home', views.Home, name="contact")
]