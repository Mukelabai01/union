from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('news/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('appointment/', create_appointment, name='create_appointment'),
    path('success/', success_view, name='success_view'),

    
   
]