from rest_framework import viewsets

from django.contrib.auth import User

from app.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
