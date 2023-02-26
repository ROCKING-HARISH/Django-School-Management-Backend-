from rest_framework import serializers
from UserAccount.models import UserProfile

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
