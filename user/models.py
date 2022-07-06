from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    about = models.TextField(max_length=100,null=True,blank=True)
    student = models.BooleanField(default=False)

    def __str__(self):
        return self.user

YEARS=[('First',1),('Second',2),('Third',3),('Fourth',4),('Fifth',5),('Sixth',6)]

class StudentDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    college = models.CharField(max_length=200,null=True,blank=True)
    branch = models.CharField(max_length=200)
    year = models.CharField(max_length=10,choices=YEARS,default='First')
    freelancing = models.BooleanField(default=False)
    exp = models.IntegerField(default=0)

    def __str__(self):
        return self.user
