from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import views as views_auth

'''
cancle
signup to create admin 

'''
def signup(request):
    if request.method=='POST':
     
        form=CreateUserForm(request.POST)
        
        if form.is_valid():
             form.save()
             return redirect('login')
        else:
            form=CreateUserForm(request.POST)     
    else:
        form=CreateUserForm() 

    return render(request,'registration/signup.html',{'form':form})  



