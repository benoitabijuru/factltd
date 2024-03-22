from django.shortcuts import render

def index(request):
    return render(request, 'FactWebApp/index.html')

def services(request):
    return render(request, 'FactWebApp/services.html')
