from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('<str:link_slug>/', root_link,name='root-link'),
]