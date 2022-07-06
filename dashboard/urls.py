from django.urls import path
from . import views

urlpatterns = [
    path('',views.profile),
    path('dashboard/',views.dashboard),
    path('works/',views.works),
]
