from django.shortcuts import render
from django.http import JsonResponse
from .models import *
def index(request):
    home_category = ImageCategory.objects.get(name='home')  # Assuming 'home' is the name of the home category
    images = Image.objects.filter(category=home_category)
    return render(request, 'FactWebApp/index.html', {'images': images})

def about(request):
    mission_category = ImageCategory.objects.get(name='Mission')
    approach_category = ImageCategory.objects.get(name='Approach')

    mission_images = Image.objects.filter(description__icontains='mission', category=mission_category)
    approach_images = Image.objects.filter(description__icontains='approach', category=approach_category)
    
    return render(request, 'FactWebApp/about.html', {'mission_images': mission_images, 'approach_images': approach_images})

def services(request):
    home_category = ImageCategory.objects.get(name='home') 
    images = Image.objects.filter(category=home_category)
    return render(request, 'FactWebApp/services.html')

def contact(request):
    return render(request, 'FactWebApp/contact.html')

def save_contact_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', '')  # Subject is optional
        message = request.POST.get('message')
        # Save the contact message to the database
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        # Return a JSON response indicating success
        return JsonResponse({'success': True, 'message': 'Your message is sent.'})
    elif request.method == 'GET':
        # Return a JSON response indicating that GET requests are not allowed
        return JsonResponse({'success': False, 'message': 'GET requests are not allowed.'})

def team(request):
    return render(request, 'FactWebApp/team.html')

def news(request):
    return render(request, 'FactWebApp/news.html')

from django.shortcuts import render
from .models import Image, ImageCategory

def design(request):
    design_category = ImageCategory.objects.get(name='design')  # Assuming 'design' is the name of the design category
    design_images = Image.objects.filter(category=design_category)
    return render(request, 'FactWebApp/design.html', {'design_images': design_images})

def video(request):
    videos = Video.objects.all()  # Fetch all videos from the database
    return render(request, 'FactWebApp/video.html', {'videos': videos})

def careers(request):
    try:
        team_category = ImageCategory.objects.get(name='Team')
        board_category = ImageCategory.objects.get(name='Board')

        team_images = Image.objects.filter(category=team_category)
        board_images = Image.objects.filter(category=board_category)
    except ImageCategory.DoesNotExist:
        # Handle the case where the 'Team' or 'Board' category does not exist
        team_images = []
        board_images = []
    
    return render(request, 'FactWebApp/careers.html', {'team_images': team_images, 'board_images': board_images})

def research(request):
    lab_images = Image.objects.filter(category__name='lab')
    study_images = Image.objects.filter(category__name='study')
    tool_images = Image.objects.filter(category__name='tool')
    training_images = Image.objects.filter(category__name='training')
    return render(request, 'FactWebApp/research.html', {
        'lab_images': lab_images,
        'study_images': study_images,
        'tool_images': tool_images,
        'training_images': training_images,
       
    
    }
    )