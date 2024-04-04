from django.shortcuts import render

def index(request):
    return render(request, 'FactWebApp/index.html')

def about(request):
    return render(request, 'FactWebApp/about.html')

def services(request):
    return render(request, 'FactWebApp/services.html')

def contact(request):
    return render(request, 'FactWebApp/contact.html')

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