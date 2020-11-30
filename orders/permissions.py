from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    """
    CRUD of Owner user to his announcements
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_owner

    def has_object_permission(self, request, view, obj):

        return (request.user and request.user.is_authenticated
                and request.user == obj.owner)