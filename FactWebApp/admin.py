#from .models import team_image
from django.contrib import admin
from .models import Image;
from .models import ImageCategory;
from .models import ContactMessage;
from .models import Service;
from .models import Video;



#customizing admin panel
admin.site.register(Image)
admin.site.register(ImageCategory)
admin.site.register(ContactMessage)
admin.site.register(Video)
admin.site.register(Service)








