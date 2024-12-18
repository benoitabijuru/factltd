from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class ImageCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, default='Title')
    description = models.TextField()
    location = models.CharField(max_length=100, default='Location')
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Name')  
    role = models.CharField(max_length=100, default='Role')
    posted_date = models.DateTimeField(default=now) # Default to the current date/time
    magazine_type=models.TextField(default='Architectural magazine')
    service_title=models.CharField(max_length=100,default='Architectural and construction service') 
    service_Description=models.TextField()  

    def clean(self):
        """Custom validation to ensure posted_date is not in the future."""
        if self.posted_date > now():
            raise ValidationError("Posted date cannot be in the future.")

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Services(models.Model):
    service_title = models.CharField(max_length=150, default="Default Service Title")  # Default title
    image = models.ImageField(upload_to='images/',blank=True,null=True)  # Default image path
    description = models.TextField(default="this services is provided by Fact ltd, which is located in Kigali.") 
    

    def __str__(self):
        return self.service_title

class Video(models.Model):
    video_file = models.FileField(upload_to='videos/') # Upload path for videos
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True) 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title