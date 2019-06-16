from rest_framework import serializers
from manageHours.models import RequestInvitation, Task, Week, Member
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class WeekSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

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


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('member_id', 'week_id')


class WeekTaskSerializer(serializers.ModelSerializer):
    """
        serializador del modelo week que trae
        con esta las tareas correspondiente que contiene
    """
    tasks = TaskSerializer(source='task_set', many=True)

    class Meta:
        model = Week
        fields = ('id', 'start_date', 'end_date', 'tasks')


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='user_id')
    weeks = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ('id', 'user', 'weeks')

    def get_weeks(self, member):
        week = Member.objects.get(pk=member.user_id_id) \
                             .team_id.week_set \
                             .filter(user_id_id=member.user_id_id)
        return WeekTaskSerializer(week, many=True).data
