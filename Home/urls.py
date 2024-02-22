from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('CitizenReport', views.CitizenReport, name="Citizen"),
    path('Anekal',views.Anekal, name = 'Anekal'),
    path('Banashankari',views.Banashankari, name = 'Banashankari'),
    path('Yelahanka',views.Yelahanka, name = 'Yelahanka'),
    path('db',views.data, name = 'database'),
    

    # path('', views.about, name="about"),
    # path('contact', views.contact, name="contact"),
    # path('Home', views.Home, name="contact")
    

]