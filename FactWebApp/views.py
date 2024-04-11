from django.shortcuts import render
from .models import homeImage
from .models import aboutImages
from .models import designImages
from .models import designLabImages, studiesImages, toolsImages, trainingImages

def index(request):
    images = homeImage.objects.all()
    return render(request, 'FactWebApp/index.html', {'images': images})

def about(request):
    mission_images = aboutImages.objects.filter(description__icontains='mission')
    approach_images = aboutImages.objects.filter(description__icontains='approach')
    return render(request, 'FactWebApp/about.html', {'mission_images': mission_images, 'approach_images': approach_images})

def services(request):
    return render(request, 'FactWebApp/services.html')

def contact(request):
    return render(request, 'FactWebApp/contact.html')

def team(request):
    return render(request, 'FactWebApp/team.html')

def news(request):
    return render(request, 'FactWebApp/news.html')

def design(request):
    design_images = designImages.objects.all()  
    category = request.GET.get('category')
    if category:
        design_images = designImages.objects.filter(category=category)
    return render(request, 'FactWebApp/design.html', {'design_images': design_images})

def video(request):
    return render(request, 'FactWebApp/video.html')

def careers(request):
    return render(request, 'FactWebApp/careers.html')

def research(request):
    lab_images = designLabImages.objects.all()
    study_images = studiesImages.objects.all()
    tool_images = toolsImages.objects.all()
    training_images = trainingImages.objects.all()
    return render(request, 'FactWebApp/research.html', {
        'lab_images': lab_images,
        'study_images': study_images,
        'tool_images': tool_images,
        'training_images': training_images
    })

def sales(request):
    return render(request, "FactWebApp/sales.html")

def checkout(request):
    return render(request, "FactWebApp/checkout.html")