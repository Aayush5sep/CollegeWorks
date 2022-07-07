from django.shortcuts import redirect, render
from django.contrib import messages
from user.models import UserDetails

def profile(request):
    if request.user.is_authenticated:
        userd=UserDetails.objects.get(user=request.user)
        return render(request,'dashboard/profile.html',{'userd':userd})
    else:
        messages.error(request,"Kindly Log In")
        return redirect("/user/loginpage")

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard/dashboard.html')
    else:
        messages.error(request,"Kindly Log In")
        return redirect("/user/loginpage")

def works(request):
    if request.user.is_authenticated:
        return render(request,'dashboard/works.html')
    else:
        messages.error(request,"Kindly Log In")
        return redirect("/user/loginpage")