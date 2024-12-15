from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('list/',trip_list,name='trip-list'), ]