from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

class CreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)