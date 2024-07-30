from rest_framework import serializers
from .models import Task
from projects.models import Project
from users.serializers import UserSerializer
from projects.serializers import ProjectSerializer

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Task
        fields = '__all__'
