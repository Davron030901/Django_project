from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('<int:pk>/', job_detail,name='job-detail'),
]