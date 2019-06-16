from rest_framework.routers import DefaultRouter
from manageHours.views import RequestViewset, ReportViewset, TaskView
from django.urls import path


router = DefaultRouter()
router.register('reports', ReportViewset, base_name='reports')
router.register('requests', RequestViewset, base_name='requests')
urlpatterns = [
    path(
        'tasks',
        TaskView.as_view()
    ),
]

urlpatterns += router.urls
