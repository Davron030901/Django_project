from rest_framework.routers import DefaultRouter
from .views import PillViewSet

router = DefaultRouter()

router.register(r'pull', PillViewSet)