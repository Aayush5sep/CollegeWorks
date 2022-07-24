from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    msg = models.TextField(max_length=1000)

    def __str__(self):
        return self.name