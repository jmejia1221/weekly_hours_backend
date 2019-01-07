from rest_framework.routers import DefaultRouter
from manageHours.views import RequestViewset, ReportViewset


router = DefaultRouter()
router.register('reports', ReportViewset, base_name='reports')
router.register('requests', RequestViewset, base_name='requests')
urlpatterns = router.urls