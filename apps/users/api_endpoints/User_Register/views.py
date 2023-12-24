from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer
from apps.users.models import User


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


__all__ = ['UserRegisterAPIView']
