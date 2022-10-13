from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import ContactUs
from django.conf import settings

def error(request):
    return render(request,'error.html')

def index(request):
    return render(request,'index.html')

def msg(request):
    name = request.POST['name']
    email = request.POST['email']
    msg = request.POST['msg']
    message = ContactUs(name=name,email=email,msg=msg)
    message.save()
    return redirect('/')

def allmsg(request):
    if request.user.is_staff:
        msgs = ContactUs.objects.all()
        return render(request,'allmsg.html',{'msgs':msgs})
    return HttpResponse("You are not allowed to view this page")

def error_404_view(request, exception):
    return render(request, 'error.html')