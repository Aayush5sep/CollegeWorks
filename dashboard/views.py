from django.shortcuts import render

def profile(request):
    return render(request,'dashboard/profile.html')

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def works(request):
    return render(request,'dashboard/works.html')