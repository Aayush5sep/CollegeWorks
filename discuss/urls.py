from django.urls import path
from . import views

urlpatterns = [
    path('',views.discusshome),
    path('qn/<int:dbtid>',views.doubt),
    path('temp/',views.temp),
]