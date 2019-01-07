from rest_framework import serializers
from manageHours.models import RequestInvitation, Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('')
        fields = ('id')
    


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestInvitation
        fields = '__all__'
        depth = 1


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        depth = 2
        

# http://weeklyhours-luism0reno.c9users.io:8080/team/1/
class TeamReportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestInvitation
        fields = '__all__'

        
