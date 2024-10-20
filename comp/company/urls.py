from django.urls import path
from .views import *
urlpatterns = [
	path('', about, name='about'),
	path('report/', report, name='report'),
	path('employees_info/', employees_info, name='employees-info'),
]