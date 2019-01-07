from django.db import models
from django.contrib.auth.models import User


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
    
    def __str__(self):
        return '{0} - {1}'.format(self.user_id.username, self.team_id.name)
    

class Week(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    def __str__(self):
        return se
    

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
    
