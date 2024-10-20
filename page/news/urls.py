from django.urls import path
from .views import HomePostView
urlpatterns = [
    path('', HomePostView.as_view(), name='home'),
]