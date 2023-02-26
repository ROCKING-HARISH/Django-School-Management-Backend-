from django.shortcuts import render
from Profile.serializers import StudentProfileSerializer
from Profile.models import StudentProfile

# Create your views here.
from rest_framework import generics
from .models import TimeTable
from .serializers import TimeTableSerializer

class TimeTableByClassYearWeekday(generics.ListAPIView):
    serializer_class = TimeTableSerializer

    def get_queryset(self):
        class_year = self.kwargs['class_year']
        weekday = self.kwargs['weekday']
        return TimeTable.objects.filter(class_year=class_year, weekday=weekday)

class TimeTableByTeacherIdWeekday(generics.ListAPIView):
    serializer_class = TimeTableSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        weekday = self.kwargs['weekday']
        return TimeTable.objects.filter(teacher_id=teacher_id, weekday=weekday)

class StudentByClassYear(generics.ListAPIView):
    serializer_class = StudentProfileSerializer

    def get_queryset(self):
        class_year = self.kwargs['class_year']
        return StudentProfile.objects.filter(class_year=class_year)
