from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PillSerializer
from .models import PILL
from rest_framework import permissions

class PillViewSet(ModelViewSet):
    queryset =PILL.objects.all()
    serializer_class =PillSerializer
    permission_classes = (permissions.AllowAny,)


