from django.contrib import admin

from FactWebApp.views import services
from .models import Image, ImageCategory
from .models import ContactMessage
from .models import Service
from .models import Video
#from .models import team_image



admin.site.register(Image)
admin.site.register(ImageCategory)
admin.site.register(ContactMessage)
admin.site.register(Service)
admin.site.register(Video)







