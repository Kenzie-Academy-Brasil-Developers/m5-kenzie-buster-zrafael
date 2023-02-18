from rest_framework import permissions
from rest_framework.views import Request, View

class TokenPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.user.is_authenticated:
            return True
        return False