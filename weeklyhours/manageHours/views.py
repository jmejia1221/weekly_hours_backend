from rest_framework import viewsets
from manageHours.models import RequestInvitation, Task
from manageHours.serializers import RequestSerializer, TeamReportsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter



class RequestViewset(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    queryset = RequestInvitation.objects.all()
    
    def get_queryset(self):
        return RequestInvitation.objects.all().filter(team_id__leader_id=self.request.user).order_by('-created')


class ReportViewset(viewsets.ModelViewSet):
    serializer_class = TeamReportsSerializer
    queryset = Task.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('day',)
    filter_fields = ('description', 'week_id__start_date')
