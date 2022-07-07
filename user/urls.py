from django.urls import path
from . import views

urlpatterns = [
    path('loginpage',views.loginpage),
    path('signuppage',views.signuppage),
    path('signup/',views.signupuser),
    path('login/',views.loginuser),
    path('logout/',views.logoutuser),
    path('profileupdate/',views.profileupdate),
    path('temp/',views.temp),
]