from rest_framework import permissions
from projects.models import Membership

class IsProjectMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            Membership.objects.get(user=request.user, project=obj.project)
            return True
        except Membership.DoesNotExist:
            return False
