from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверяет является пользователь владельцем привычки."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
