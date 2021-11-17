from django.urls import path

from . import views
app_name='notifcation'
urlpatterns = [

   
  path('note/<uuid:unique_id>', views.send_notication.as_view(),name='notefication'),
   
]
