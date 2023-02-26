from django.db import models
from django.contrib.auth.models import User

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add other fields here

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_year = models.IntegerField(blank=True, null=True)
