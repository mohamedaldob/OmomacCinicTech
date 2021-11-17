from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import path

from accounts import forms,views
from . import views
app_name='account'
urlpatterns = [
  path('signup',views.signup,name='signup'),
  

]
