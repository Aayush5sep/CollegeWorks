from django.contrib import admin
from .models import Subjects,Books,Notes,Exams,Experiments,Assignments,Projects

# Register your models here.

admin.site.register(Subjects)
admin.site.register(Books)
admin.site.register(Notes)
admin.site.register(Experiments)
admin.site.register(Exams)
admin.site.register(Assignments)
admin.site.register(Projects)