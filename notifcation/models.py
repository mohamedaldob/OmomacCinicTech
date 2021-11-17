import uuid
from django.db import models
from datetime import datetime


'''
model notifaction upload image to folder of week
contain artical of week 


'''
   
def impage_upload(instance,filename):
        imagename,extension=filename.split(".")
        return 'image_note/%s/%s.%s'%(str(instance.number_week),str(imagename),str(extension))

class notefication(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    notfication=models.CharField(max_length=200)    
    content_note=models.TextField(max_length=2500,)
    number_week=models.IntegerField()
    number_month=models.IntegerField()
    img_note= models.ImageField(upload_to=impage_upload)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
            return "(notefication of week"+str(self.number_week)+")( and month :"+str(self.number_month)+" )"
    
    class Meta:
          ordering = ['number_week']
    
    
    
    
   