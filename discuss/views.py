from django.shortcuts import render
from .models import Discussions, Doubt
from search import searchlist

# Create your views here.

def discusshome(request):
    latest = Doubt.objects.order_by('-time')[:5]
    return render(request,'discuss/discusshome.html',{'latest':latest})

def doubt(request,dbtid):
    question = Doubt.objects.get(id=dbtid)
    discussions = Discussions.objects.filter(post=dbtid)
    return render(request,'discuss/question.html',{'qn':question,'dcns':discussions})

def search(request):
    query=request.GET.get('search').lower()
    mylist=[]
    for dbt in Doubt.objects.all():
        strn=str(dbt.id) + " " + dbt.title.lower() + " " + dbt.question.lower()
        print(strn)
        mylist.append(strn)
    result = searchlist(mylist,query,4)
    mylist=[]
    for res in result:
        rid = int(res.split()[0])
        dbt = Doubt.objects.get(id=rid)
        mylist.append(dbt)
    return render(request,'discuss/discusshome.html',{'latest':mylist})
    


def temp(request):
    return render(request,'discuss/question.html')
