from django.urls import path
from .views import *
urlpatterns = [
    path('',getData),
    path('add/',addItem),
]