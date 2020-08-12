from rest_framework.permissions import BasePermission


class PublicPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or view.action in ['list', 'retrieve']


class PrivatePermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
