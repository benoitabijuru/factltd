from django.contrib import admin

from FactWebApp.views import services
from .models import Image, ImageCategory
from .models import ContactMessage
from .models import Service

admin.site.register(Image)
admin.site.register(ImageCategory)
admin.site.register(ContactMessage)
admin.site.register(Service)





