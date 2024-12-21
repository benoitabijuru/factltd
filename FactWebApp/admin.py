#from .models import team_image
from django.contrib import admin
from .models import Image;
from .models import ImageCategory;
from .models import ContactMessage;
from .models import Video;


#customizing admin panel
#admin.site.register(Image)
admin.site.register(ImageCategory)
admin.site.register(ContactMessage)
admin.site.register(Video)
from django.contrib import admin
from .models import Image, ImageCategory

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'posted_date')
    list_filter = ('category', 'subcategory')
    search_fields = ('title', 'description')







