from rest_framework import serializers
from .models import Project, Membership
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model

class MembershipSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Membership
        fields = ['user', 'project', 'role']


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    members = MembershipSerializer(source='membership_set', many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

