from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('send-message/', views.send_message, name='send_message'),
    path('menu/', views.menu, name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('flavors/', views.flavors, name='flavors'),
    path('order/', views.order, name='order'),
]
