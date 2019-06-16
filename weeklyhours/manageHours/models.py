from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Team(models.Model):
    name = models.CharField(max_length=50)
    leader_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Member(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username


class RequestInvitation(models.Model):
    pending = models.BooleanField(default=True)
    accepted = models.BooleanField(default=False)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} - {1}'.format(self.user_id.username, self.team_id.name)


class Week(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - {1} - Team: {2}'.format(self.start_date,
                                              self.end_date,
                                              self.team_id.name)


class Task(models.Model):
    DAYS = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('TH', 'Thursday'),
        ('F', 'Friday'),
        ('S', 'Saturday'),
        ('SU', 'Sunday')
    )
    description = models.CharField(max_length=255)
    amount_hours = models.PositiveIntegerField()
    day = models.CharField(max_length=2, choices=DAYS)
    week_id = models.ForeignKey(Week, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - Description: {1}'.format(self.member_id.user_id.username,
                                               self.description)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
