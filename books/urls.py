from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('category/<str:subject>',views.resources),
    path('temp/',views.temp),
    path('respage/',views.respage),
    path('addnew/',views.addnew),
    path('api/', views.BookList.as_view()),
]