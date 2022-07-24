from django.shortcuts import redirect, render
from .models import ContactUs

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
    msgs = ContactUs.objects.all()
    return render(request,'allmsg.html',{'msgs':msgs})