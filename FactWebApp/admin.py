from django.contrib import admin
from .models import homeImage
from .models import aboutImages
from .models import designImages
from .models import designLabImages, studiesImages, toolsImages, trainingImages

admin.site.register(homeImage)
admin.site.register(aboutImages)
admin.site.register(designImages)
admin.site.register(designLabImages)
admin.site.register(studiesImages)
admin.site.register(toolsImages)
admin.site.register(trainingImages)



