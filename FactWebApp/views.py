from django.shortcuts import render
from .models import Image

def index(request):
    image = Image.objects.first()
    return render(request, 'FactWebApp/index.html', {'image': image})

def about(request):
    return render(request, 'FactWebApp/about.html')

def services(request):
    return render(request, 'FactWebApp/services.html')

def contact(request):
    return render(request, 'FactWebApp/contact.html')

def team(request):
    return render(request, 'FactWebApp/team.html')

def news(request):
    return render(request, 'FactWebApp/news.html')

def design(request):
    return render(request, 'FactWebApp/design.html')

def video(request):
    return render(request, 'FactWebApp/video.html')

def careers(request):
    return render(request, 'FactWebApp/careers.html')

def research(request):
    return render(request, 'FactWebApp/research.html')

def sales(request):
    return render(request, "FactWebApp/sales.html")

def checkout(request):
    return render(request, "FactWebApp/checkout.html")