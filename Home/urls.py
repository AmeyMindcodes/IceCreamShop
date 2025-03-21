from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('visit/', views.visit, name='visit'),
]

# from django.contrib import admin
# from django.urls import path
# from Home import views

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('about/', views.about, name='about'),  # Added trailing slash
#     path('services/', views.services, name='services'),  # Added trailing slash
#     path('contact/', views.contact, name='contact'),  # Added trailing slash
#     path('send_message/', views.send_message, name='send_message'),  # Already correct
# ]
