from django.shortcuts import render

def index(request):
    return render(request, 'FactWebApp/index.html')

def about(request):
    return render(request, 'FactWebApp/about.html')

def services(request):
    return render(request, 'FactWebApp/services.html')

def contact(request):
    return render(request, 'FactWebApp/contact.html')