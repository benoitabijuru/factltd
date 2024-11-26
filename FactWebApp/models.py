from django.db import models

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

class Service(models.Model):
    service_title = models.CharField(max_length=150, default="Default Service Title")  # Default title
    image = models.ImageField(upload_to='media/images')  # Default image path
    description = models.TextField(default="this services is provided by Fact ltd, which is located in Kigali.")  # Default description

    def __str__(self):
        return self.service_title



class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/')  # Upload path for videos
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title