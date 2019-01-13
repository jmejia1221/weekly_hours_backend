from .views import CreateUser
from django.urls import path


urlpatterns = [
    path(
        'user',
        CreateUser.as_view(),
        name='user-list'
    ),
]