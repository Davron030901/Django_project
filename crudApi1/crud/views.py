from rest_framework.viewsets import ModelViewSet
from .serializers import CRUDSerializer
from .models import CRUD
from rest_framework import permissions

class CRUDViewSet(ModelViewSet):
    queryset = CRUD.objects.all()
    serializer_class =CRUDSerializer
    permission_classes = (permissions.AllowAny,)

# Create your views here.
