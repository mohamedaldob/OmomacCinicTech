from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import notefication


#get notefication by id=number_week
class send_notication(APIView):
     
      def get(self,request,unique_id):
          notefication_list=notefication.objects.filter(number_week=unique_id)
          Serializer=Note_Serializers(notefication_list,many=True)  
          return Response(Serializer.data)