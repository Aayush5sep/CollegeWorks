from django.db import models

# Create your models here.

class Books(models.Model):

    YEARS=[('First',1),('Second',2),('Third',3),('Fourth',4),('Fifth',5),('Sixth',6)]

    title = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=100, default='')
    branch_subject = models.CharField(max_length=50, null=False)
    specific_subject = models.CharField(max_length=100, null=False)
    year = models.CharField(max_length=10,choices=YEARS,default='First')
    link = models.URLField(max_length=200)
    updated = models.DateTimeField(auto_now_add=True)
    relevancy = models.FloatField(default=0)
    # img = models.ImageField()

    def __str__(self):
        return self.title

# code to download multiple books at once
