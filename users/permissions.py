from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Account

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False

class IsAccountOwnerOrIsEmployee(permissions.BasePermission):
    def has_object_permission(self, request:Request, view: View, obj: Account):
        return request.user.is_authenticated and (request.user == obj or request.user.is_employee)