from django.shortcuts import render

# Create your views here.

def discusshome(request):
    return render(request,'discuss/discusshome.html')

def temp(request):
    return render(request,'discuss/question.html')
