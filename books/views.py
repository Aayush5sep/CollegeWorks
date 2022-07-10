from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from books.models import Books,Subjects,Notes,Exams,Experiments,Assignments,Projects
# from rest_framework.decorators import api_view
# from django.views.decorators.csrf import csrf_exempt
from books.serializers import BookSerializer
from rest_framework.views import APIView
# from rest_framework import status

# Create your views here.

def homepage(request):
    subjects=Subjects.objects.all()
    first=subjects.filter(year="First").order_by('branch_subject')
    second=subjects.filter(year="Second").order_by('branch_subject')
    third=subjects.filter(year="Third").order_by('branch_subject')
    fourth=subjects.filter(year="Fourth").order_by('branch_subject')
    fifth=subjects.filter(year="Fifth").order_by('branch_subject')
    sixth=subjects.filter(year="Sixth").order_by('branch_subject')
    params={'first':first,'second':second,'third':third,'fourth':fourth,'fifth':fifth,'sixth':sixth}
    return render(request,'books/collectionhome.html',params)

# Books,Subjects,Notes,Exams,Experiments,Assignments,Projects
def resources(request,subject):
    books = Books.objects.filter(branch_subject=subject).order_by('title')
    notes = Notes.objects.filter(branch_subject=subject).order_by('topic')
    exams = Exams.objects.filter(branch_subject=subject).order_by('topic')
    experiments = Experiments.objects.filter(branch_subject=subject).order_by('topic')
    assignments=Assignments.objects.filter(branch_subject=subject).order_by('topic')
    params={'books':books,'notes':notes,'exams':exams,'experiments':experiments,'assignments':assignments}
    return render(request,'books/subject.html',params)

class BookList(APIView):
    def get(self, request):
        snippets = Books.objects.all()
        serializer = BookSerializer(snippets, many=True)
        return Response(serializer.data)
    def post(self, request):
        # serializer = BookSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        snippets = Books.objects.all()
        serializer = BookSerializer(snippets, many=True)
        return Response(serializer.data)

# @csrf_exempt
# @api_view(['GET','POST'])
# GET,POST,PUT,DELETE
# def book_list(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#     allbooks = Books.objects.all()
#     serializer = BookSerializer(allbooks, many=True)
#     return JsonResponse(serializer.data, safe=False)



# def book_list(request):
#     allbooks = Books.objects.all()
#     serializer = BookSerializer(allbooks, many=True)
#     if serializer.is_valid():
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def temp(request):
    return render(request,'books/subject.html')