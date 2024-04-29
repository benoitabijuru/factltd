from django.contrib import admin
from .models import Image, ImageCategory
from .models import ContactMessage

admin.site.register(Image)
admin.site.register(ImageCategory)
admin.site.register(ContactMessage)



