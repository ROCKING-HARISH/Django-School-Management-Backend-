from django.db import models
from Profile.models import TeacherProfile, StudentProfile

# Create your models here.
class TimeTable(models.Model):
    class_year = models.IntegerField()
    weekday = models.CharField(max_length=20)
    start_time = models.TimeField()
    subject_name = models.CharField(max_length=100)
    teacher_id = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=50, blank=True, null=True, default="NA")