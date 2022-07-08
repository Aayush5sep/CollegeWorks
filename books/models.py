from django.db import models

# Create your models here.
YEARS=[('First',1),('Second',2),('Third',3),('Fourth',4),('Fifth',5),('Sixth',6)]

class Subjects(models.Model):
    branch_subject=models.TextField(max_length=50)
    year=models.CharField(max_length=10,choices=YEARS,default='First')

    def __str__(self):
        return self.branch_subject

class Books(models.Model):

    title = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=100, default='')
    branch_subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    specific_subject = models.CharField(max_length=50, null=False)
    year = models.CharField(max_length=10,choices=YEARS,default='First')
    link = models.URLField(max_length=200)
    updated = models.DateTimeField(auto_now_add=True)
    relevancy = models.FloatField(default=0)
    # img = models.ImageField()

    def __str__(self):
        return self.title

# code to download multiple books at once

class Notes(models.Model):
    topic = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=50, default='')
    branch_subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    specific_subject = models.CharField(max_length=50, null=False)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.topic

class Assignments(models.Model):
    topic = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=50, default='')
    branch_subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    specific_subject = models.CharField(max_length=50, null=False)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.topic

class Projects(models.Model):
    topic = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=50, default='')
    branch_subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    specific_subject = models.CharField(max_length=50, null=False)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.topic

class Exams(models.Model):
    topic = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=50, default='')
    branch_subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    specific_subject = models.CharField(max_length=50, null=False)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.topic

class Experiments(models.Model):
    topic = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=50, default='')
    branch_subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    specific_subject = models.CharField(max_length=50, null=False)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.topic
