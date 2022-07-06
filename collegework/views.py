from django.shortcuts import render

def error(request):
    return render(request,'error.html')

def index(request):
    return render(request,'index.html')