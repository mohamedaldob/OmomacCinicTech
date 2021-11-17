from rest_framework import serializers
from .models import *

        
class Note_Serializers(serializers.ModelSerializer):
      class Meta:
          model=notefication
          fields='__all__'                    