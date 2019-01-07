from rest_framework import serializers
from manageHours.models import RequestInvitation, Task, Week
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)
    

class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestInvitation
        fields = '__all__'
        depth = 1


class TeamReportsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    week = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_user(self, obj):
        user = User.objects.get(id=obj.member_id.user_id.pk)
        return UserSerializer(user).data
    
    def get_week(self, task):
        week = Week.objects.get(id=task.week_id.pk)
        return WeekSerializer(week).data