from django.urls import path,include
from . import views

urlpatterns = [
    path('loginpage',views.loginpage),
    path('signuppage',views.signuppage),
    path('signupdetails',views.signupdetails),
    path('login/',views.login),
]