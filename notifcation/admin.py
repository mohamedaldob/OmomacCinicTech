from django.contrib import admin
from .models import *

class admin_note(admin.ModelAdmin):
    list_display=['number_week','created','number_month']
    search_fields=['number_week']
    list_filter=['number_week'] 



admin.site.register(notefication,admin_note)

# Register your models here.
admin.site.site_header='OmOma clinic'
admin.site.site_title='OmOma clinic'
