from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Todo
from .serializers import TodoSerializer

class TodoListView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
