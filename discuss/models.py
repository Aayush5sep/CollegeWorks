from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doubt(models.Model):
    title = models.CharField(max_length=25)
    question = models.TextField(max_length=500)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='doubts/',null=True)

    def __str__(self):
        return self.title

class Discussions(models.Model):
    post = models.ForeignKey(Doubt,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    votes = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='doubts/',null=True)

    def __str__(self):
        return self.post

