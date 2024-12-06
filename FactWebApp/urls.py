from django.urls import path
from FactWebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('save-contact-message/', views.save_contact_message, name='save_contact_message'),
    path('news/', views.news, name='news'),
    path('design/', views.design, name='design'),
    path('video/', views.video, name='video'),
    path('careers/', views.careers, name='careers'),
    path('research/', views.research, name='research')
]

urlpatterns=urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
