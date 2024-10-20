from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # faqtgina ko'rish uchun ruxsat
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user