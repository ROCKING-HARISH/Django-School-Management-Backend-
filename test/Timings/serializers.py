from rest_framework import serializers
from Timings.models import TimeTable

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = ['class_year', 'weekday', 'start_time', 'subject_name', 'teacher_id']
