from django.contrib import admin
from manageHours.models import Member, RequestInvitation, Task, Team, Week


admin.site.register(Member)
admin.site.register(RequestInvitation)
admin.site.register(Task)
admin.site.register(Team)
admin.site.register(Week)