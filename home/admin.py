from django.contrib import admin
from .models import User,Visiting,Image_visiting





admin.site.register(Visiting)
admin.site.register(Image_visiting,)
# Register your models here.
admin.site.site_header='OmOma clinic'
admin.site.site_title='OmOma clinic'
