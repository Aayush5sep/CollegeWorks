from django.db import models
from django.contrib.auth.models import User

# Create your models here.

YEARS = [('First',1),('Second',2),('Third',3),('Fourth',4),('Fifth',5),('Sixth',6)]

class Requests(models.Model):
    raiser = models.ForeignKey(User,on_delete=models.CASCADE,related_name='request_raiser')
    description = models.TextField(max_length=100,blank=True)
    time = models.DateTimeField(auto_now_add=True,null=True)
    deadline = models.DateTimeField(blank=True,null=True)
    amount = models.IntegerField(blank=True,null=True)
    assigned = models.ForeignKey(User,null=True,on_delete=models.DO_NOTHING,related_name='task_assigned_to')
    completed = models.BooleanField(default=False)
    # doc = models.FileField()

    def __str__(self):
        return self.raiser


class WorkmanDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    works = models.IntegerField(default=0)
    workxp = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    failed = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class Completed(models.Model):
    completor = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True,null=True)
    workxp = models.IntegerField(default=0)