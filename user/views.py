from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import UserDetails

# Create your views here.

def loginpage(request):
    return render(request,'user/login.html')

def signuppage(request):
    return render(request,'user/signup.html')

def signupuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cfpassword=request.POST['cfpassword']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']

        if password != cfpassword:
            messages.error(request,"Passwords do not match")
            return redirect("/user/signuppage")

        newuser = User.objects.create_user(username,email,password)
        newuser.first_name=fname
        newuser.last_name=lname
        newuser.save()
        user=authenticate(username=username,password=password)
        login(request,user)
        userd=UserDetails(user=user,fname=fname,lname=lname)
        userd.save()
        messages.success(request,"User Account Created Successfully")
        return render(request,'user/signup profile.html')
    else:
        return HttpResponse("Creating new user account failed !")

def temp(request):
    return render(request,'user/signup profile.html')

def profileupdate(request):
    user = request.user
    phone = request.POST['phone']
    age = request.POST['age']
    about = request.POST['about']
    is_student = request.POST.get('is_student')
    student = False
    if is_student is not None:
        student=True
    profiled = UserDetails.objects.get(user=user)
    profiled.phone = phone
    profiled.age = age
    profiled.about = about
    profiled.student = student
    profiled.save()
    messages.success(request,'Profile Updated')
    return redirect("/")

def nameupd(request):
    if request.method=='POST':
        user = request.user
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        about=request.POST['about']
        profiled = UserDetails.objects.get(user=user)
        profiled.about = about
        profiled.fname=fname
        profiled.lname=lname
        profiled.save()
        messages.success(request,'Profile Updated')
    else:
        messages.error(request,'Insecure Request')
    return redirect("/profile/")

def contactupd(request):
    if request.method=='POST':
        user = request.user
        email=request.POST['email']
        phone=request.POST['phone']
        profiled = UserDetails.objects.get(user=user)
        profiled.phone=phone
        profiled.save()
        user.email = email
        user.save()
        messages.success(request,'Contact Updated')
    else:
        messages.error(request,'Insecure Request')
    return redirect("/profile/")

def studentupd(request):
    if request.method=='POST':
        user = request.user
        is_student=request.POST.get('is_student')
        student = False
        if is_student is not None:
            student=True
        profiled = UserDetails.objects.get(user=user)
        profiled.student=student
        profiled.save()
        messages.success(request,'Student Status Updated')
    else:
        messages.error(request,'Insecure Request')
    return redirect("/profile/")


def loginuser(request):
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

def logoutuser(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect("/")