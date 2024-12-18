from django.urls import path
from FactWebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('design/', views.design, name='design'),
    path('research/', views.research, name='research'),
    path('video/', views.video, name='video'),
    path('news/', views.news, name='news'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
    path('save-contact-message/', views.save_contact_message, name='save_contact_message'),
]

urlpatterns=urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
