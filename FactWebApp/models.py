from django.db import models

class homeImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class aboutImages(models.Model):
    image = models.ImageField(upload_to='about_images/')
    description = models.TextField()

    def __str__(self):
        return self.description
    
class designImages(models.Model):
    image = models.ImageField(upload_to='design_images/')
    title = models.CharField(max_length=100, default='Unknown')
    location = models.CharField(max_length=100, default='Unknown')
    description = models.TextField()
    category = models.CharField(max_length=100, default='Other')

    def __str__(self):
        return self.title
    
class designLabImages(models.Model):
    image = models.ImageField(upload_to='design_labs/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class studiesImages(models.Model):
    image = models.ImageField(upload_to='studies/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class toolsImages(models.Model):
    image = models.ImageField(upload_to='tools/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class trainingImages(models.Model):
    image = models.ImageField(upload_to='training/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


