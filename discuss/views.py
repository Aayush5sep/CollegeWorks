from django.shortcuts import render
from .models import Discussions, Doubt

# Create your views here.

def discusshome(request):
    latest = Doubt.objects.order_by('-time')[:5]
    return render(request,'discuss/discusshome.html',{'latest':latest})

def doubt(request,dbtid):
    question = Doubt.objects.get(id=dbtid)
    discussions = Discussions.objects.filter(post=dbtid)
    return render(request,'discuss/question.html',{'qn':question,'dcns':discussions})

def temp(request):
    return render(request,'discuss/question.html')
