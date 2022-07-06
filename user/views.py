from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def loginpage(request):
    return render(request,'user/login.html')

def signuppage(request):
    return render(request,'user/signup.html')

def signupdetails(request):
    return render(request,'user/signup profile.html')

def login(request):
    if request.method=='POST':
        login_username=request.POST['username']
        login_password=request.POST['password']

        user=authenticate(username=login_username,password=login_password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect("/")
        else:
            messages.error(request,'Login Failed')
            return HttpResponse("Oops! Login Failed")
    else:
        return HttpResponse("Unsecured Login Error !!")