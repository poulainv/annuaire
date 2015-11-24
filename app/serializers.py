from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
