from django.urls import path
from FactWebApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('design/', views.design, name='design'),
    path('video/', views.video, name='video'),
    path('careers/', views.careers, name='careers'),
    path('research/', views.research, name='research'),
    path('sales/', views.sales, name='sales'),
    path('checkout/', views.checkout, name='checkout'),
    
]
