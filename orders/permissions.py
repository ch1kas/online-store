from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    """
    Permission to view orders
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        return (request.user and request.user.is_authenticated
                and request.user == obj.owner)