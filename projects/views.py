from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Project, Membership
from .serializers import ProjectSerializer
from .serializers import MembershipSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        project = serializer.save(owner=self.request.user)
        Membership.objects.create(user=self.request.user, project=project, role='owner')

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Membership.objects.filter(project__owner=self.request.user)