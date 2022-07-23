from django.urls import path
from . import views

urlpatterns = [
    path('',views.discusshome),
    path('temp/',views.temp),
]